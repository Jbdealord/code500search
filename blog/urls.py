from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list_view, name='post_list_view'),
    url(r'^(?P<post>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
]
