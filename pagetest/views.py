from django.shortcuts import render_to_response
from pagetest.models import AreaUrl
from pagetest.GetAndPost import ExecFuc
import pagetest.GlobalVar
import operator
# Create your views here.

# 主页
def homepage(request):
    region_name = list(AreaUrl.objects.values_list('region',flat=True))
    return render_to_response('homepage.html',{'region_name':region_name})

# Get和Post拨测汇总页面
def summary(request):
    pagetest.GlobalVar.GL_GET_RESP_RIGHT = {}
    pagetest.GlobalVar.GL_GET_RESP_WARNING = {}
    pagetest.GlobalVar.GL_GET_RESP_ERROR = {}
    pagetest.GlobalVar.GL_POST_RESP_RIGHT = {}
    pagetest.GlobalVar.GL_POST_RESP_WARNING = {}
    pagetest.GlobalVar.GL_POST_RESP_ERROR = {}
    select_region = request.GET['area']
    ExecFuc(select_region)
    get_right = dict(sorted(pagetest.GlobalVar.GL_GET_RESP_RIGHT.items(),key=operator.itemgetter(0)))
    get_warning = dict(sorted(pagetest.GlobalVar.GL_GET_RESP_WARNING.items(), key=operator.itemgetter(0)))
    get_error = dict(sorted(pagetest.GlobalVar.GL_GET_RESP_ERROR.items(), key=operator.itemgetter(0)))
    post_right = pagetest.GlobalVar.GL_POST_RESP_RIGHT
    post_warning = pagetest.GlobalVar.GL_POST_RESP_WARNING
    post_error = pagetest.GlobalVar.GL_POST_RESP_ERROR
    return render_to_response('summary.html',locals())

