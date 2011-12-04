from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('portal.views',
    url(r'^$', 'index'),
    url(r'^accounts/login/?$', 'login'),
)