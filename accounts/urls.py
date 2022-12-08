from django.urls import path,re_path
from .views import *
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    # path(r'^company-edit/$', company_edit_view, name='company-edit'),
	path('register/',register,name="register"),
    path('login/', login_view, name='login'),
    # path(r'^update-profile/$', update_profile_view, name='update_profile_view'),
    # path(r'^my-account/$',account_view,name="account_view"),
    # path(r'^user-list/$',user_list_view,name="user_list_view"),
    # path(r'^user/(?P<slug>.*)/$', user_update, name='user_update'),
    path('logout/',logout_view,name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        activate, name='activate'),
]