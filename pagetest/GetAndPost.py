import requests,threading
from pagetest.QueryData import QueryFromDb
import pagetest.GlobalVar

'''
定义函数GetResoult()
1、对不同的栏目Url,执行Http-get操作
2、获取每个栏目Url执行后的“HTTP状态码”和“响应时间”（其中要处理网络连接失败的情况）
输入：name/IP地址/url路径/响应阈值
输出：没有输出，处理的结果直接写进全局变量：GL_GET_RESP_RIGHT/GL_GET_RESP_WARNING/GL_GET_RESP_ERROR

定义函数PostData()
1、模拟bnc向scsp发起post请求
2、获取scsp返回的“HTTP状态码”和“响应时间”（其中要处理网络连接失败的情况）
输入：name/post地址/post内容/响应阈值
输出：{接口名字：(HTTP状态码,响应时间)}或者{ 接口名字}
'''

def GetResoult(ip,name_path_list,threshold):

    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'Keep-Alive',
    }

    for name,path in name_path_list.items():
        get_resoult = '%s%s%s' % ('http://',ip,path)    # URL拼接
        # print(get_resoult)
        try:
            t = requests.get(get_resoult, headers=headers, timeout=0.5)     # 获取get对象
            resp_time = t.elapsed.microseconds / 1000   # 响应时间（单位：秒）
            resp_code = t.status_code       # Http状态码
            if resp_code == 200:    # 响应正常分2种情况：1、响应时间未超阈值；2、响应时间超过阈值
                if resp_time < threshold:
                    pagetest.GlobalVar.GL_GET_RESP_RIGHT[(ip,name)] = (resp_time,resp_code)
                else:
                    pagetest.GlobalVar.GL_GET_RESP_WARNING[(ip,name)] = (resp_time,resp_code)
            else:
                pagetest.GlobalVar.GL_GET_RESP_ERROR[(ip,name)] = (resp_time,resp_code)
        except:     # 实际get响应时间超过timeout,直接提示网络异常
            pagetest.GlobalVar.GL_GET_RESP_ERROR[(ip,name)] = ('Request Timedout','Network Error!')

def PostResoult(post_url,post_content,post_threshold,post_name):
    try:
        p = requests.post(url=post_url,data=post_content.encode('utf-8'))
        resp_time = p.elapsed.microseconds / 1000
        resp_code = p.status_code
        resp_content = p.text
        print(resp_code)
        if resp_code == 200:
            if resp_time < post_threshold:
                pagetest.GlobalVar.GL_POST_RESP_RIGHT[post_name] = (resp_time, resp_code)
            else:
                pagetest.GlobalVar.GL_POST_RESP_WARNING[post_name] = (resp_time, resp_code)
        else:
            pagetest.GlobalVar.GL_POST_RESP_ERROR[post_name] = (resp_time, resp_code)

    except:
        pagetest.GlobalVar.GL_POST_RESP_ERROR[post_name] = ('Request Timedout', 'Network Error!')



def ExecFuc(execfuc_region):

    query_tmp = QueryFromDb(execfuc_region)     # 通过函数QueryFromDb从数据库获取数据
    # get数据拆解
    get_name_path = query_tmp[0]    # {}
    get_ip_threshold = query_tmp[1]
    get_ip_list = get_ip_threshold['ip'].split('\r\n')
    get_threshold = get_ip_threshold['get_threshold']

    # post数据拆解
    post_data = query_tmp[2]    # {}
    #print(post_data)
    try:
        post_name = post_data['post_req_name']
        post_url = post_data['post_interface_url']
        post_content = post_data['post_content']
        post_threshold = (query_tmp[3])['post_threshold']
    except:
        pass

    threads = []        # 定义线程对象列表
    nloops = range(len(get_ip_list))        #

    if get_name_path and post_data:     # get和post都不为空字典，即get和post操作都需要执行
        for i in nloops:
            t = threading.Thread(target=GetResoult, args=(get_ip_list[i], get_name_path, get_threshold))
            threads.append(t)

        for i in nloops:
            threads[i].start()

        for i in nloops:
            threads[i].join()

        p = threading.Thread(target=PostResoult, args=(post_url, post_content, post_threshold, post_name))
        p.start()
        p.join()

    elif get_name_path:     # get不为空字典，且post为空字典，即get需要执行，且post不需要执行
        for i in nloops:
            t = threading.Thread(target=GetResoult, args=(get_ip_list[i], get_name_path, get_threshold))
            threads.append(t)

        for i in nloops:
            threads[i].start()

        for i in nloops:
            threads[i].join()
    else:     # post不为空字典，且get为空字典，即post需要执行，且get不需要执行
        p = threading.Thread(target=PostResoult, args=(post_url, post_content, post_threshold, post_name))
        p.start()
        p.join()
