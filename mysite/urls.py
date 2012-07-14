from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead
from books import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url('^hello/$', hello),
	url('^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search/$', views.search),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
