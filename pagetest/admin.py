from django.contrib import admin
from pagetest.models import GetReq,PostReq,AreaUrl


class GetReqAdmin(admin.ModelAdmin):
    list_display = ('get_req_name','get_path')
    search_fields = ('get_req_name',)
    ordering = ('get_req_name',)
    list_per_page = 50

class PostReqAdmin(admin.ModelAdmin):
    list_display = ('post_req_name','post_interface_url','post_content')
    search_fields = ('post_req_name',)
    ordering = ('post_req_name',)
    list_per_page = 50

class AreaUrlAdmin(admin.ModelAdmin):
    list_display = ('region','ip','get_threshold','post_threshold')
    search_fields = ('region','ip')
    list_filter = ('getreqs','postreq')
    ordering = ('region',)
    filter_horizontal = ('getreqs',)
    list_per_page = 50

admin.site.site_header = '拨测管理系统'
admin.site.site_title = 'CC运维'

admin.site.register(GetReq,GetReqAdmin)
admin.site.register(PostReq,PostReqAdmin)
admin.site.register(AreaUrl,AreaUrlAdmin)
