from pagetest.models import AreaUrl

def QueryFromDb(querydata_area):
    # 步骤一：获取get请求的“name和path”以及“ip和threshold”
    get_name_path = {}
    get_ip_threshold = {}
    try:
        getdata = list(AreaUrl.objects.get(region=querydata_area).getreqs.values())
        for i in range(len(getdata)):
            name = (getdata[i])['get_req_name']
            path = (getdata[i])['get_path']
            get_name_path[name] = path
        get_ip_threshold = list(AreaUrl.objects.filter(region=querydata_area).values('ip','get_threshold'))[0]
    except:
        get_name_path = {}

    # 步骤二：获取post请求的“整个字典”以及“threshold”
    post_threshold = {}
    try:
        postdata = AreaUrl.objects.get(region=querydata_area).postreq.__dict__
        post_threshold = list(AreaUrl.objects.filter(region=querydata_area).values('post_threshold'))[0]
    except:
        postdata = {}

    return get_name_path, get_ip_threshold, postdata, post_threshold
