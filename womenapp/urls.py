from django.urls import path
from .import views
from django.urls import re_path as url
urlpatterns = [
    path('',views.home,name= 'Home'),
    path("adddata/",views.adddata,name="adddata"),
    # url(r'^delete_pk/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
    path('del/<str:id>', views.delete, name = 'delete'),
    path('edit/<str:id>',views.edit,name="edit"),
    path("about/",views.about,name="about"),
]
