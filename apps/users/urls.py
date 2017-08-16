from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index,name='user_index'),
    url(r'^new$', views.new,name='user_new'),
    url(r'^create$', views.create,name='user_create'),
    url(r'^(?P<number>\d+)/edit$', views.edit,name='user_edit'),
    url(r'^(?P<number>\d+)/destroy$', views.destroy,name='user_destroy'),
    url(r'^(?P<number>\d+)/$', views.show,name='user_show'),
    
]