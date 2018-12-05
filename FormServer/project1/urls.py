from django.conf.urls import url
from project1 import views

urlpatterns = [
    url(r'^$', views.pone, name='pone_views'),

]
