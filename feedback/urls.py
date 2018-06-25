from django.conf.urls import url
from django.urls import path, include
from . import views

#urlpatterns = patterns('',url(r'^$', 'feedback.views.feedback', name='feedback'),)
urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    path('',views.feedback, name=''),
]
