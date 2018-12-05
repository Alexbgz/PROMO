from django.conf.urls import url
from formapp import views

urlpatterns = [
    url(r'^$', views.form_views, name='form_views'),
    url(r'^(?P<pk>\d+)$', views.form_detail, name='form_detail'),
]