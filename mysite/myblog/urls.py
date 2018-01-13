from django.conf.urls import url
from . import views


app_name = 'myblog'
urlpatterns = [
    url(r'^list/$',views.PostListView.as_view(),name="post_list"),
    url(r'^detail/(?P<pk>\d+)$',views.PostDetailView.as_view(),name="post_detail"),
    url(r'^create/$',views.PostCreate.as_view(),name="post_create"),
    url(r'^draft/$',views.DraftListView.as_view(),name="post_draft"),
    url(r'^register/$',views.user_register,name="user_register"),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^login/$',views.user_login,name="user_login"),
    url(r'^logout$',views.user_logout,name="user_logout"),

]
