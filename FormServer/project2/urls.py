from django.conf.urls import url
from project2 import views

urlpatterns = [
    url(r'^$', views.ptwo, name='ptwo_views'),
]
