from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'form', 'formapp.urls', name='form'),
    host(r'project1', 'project1.urls', name='project1'),
    host(r'project2', 'project2.urls', name='project2'),

)