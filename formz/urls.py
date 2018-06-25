from django.conf.urls import url
from django.urls import path, include
from . import views
urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    path('',views.get_name, name=''),
]
