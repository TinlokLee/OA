import xadmin
from xadmin import views
from .models import Department, UserProfile, Position
from xadmin.plugins.auth import Useradmin

__author__ = "Lee"

class UserProfileAdmin(Useradmin):
    list_display = ('username', 'first_name', 'last_name', 'departion', 'position')
    search_fields = ('username','first_name', 'last_name', 'departion', 'position' )
    list_filter = ('username','first_name', 'last_name', 'departion', 'position' )


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    ''' 设置页眉，页脚，风格'''
    site_title = "人事OA后台"
    site_footer = "首E家"
    nemu_style = "accordion"


@xadmin.sites.register(Department)
class DepartmentAdmin(object):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'decription')
    model_icon = "xxx xxx"


@xadmin.sites.register(Position)
class PositionAdmin(object):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'decription')
    model_icon = "xxx xxx"