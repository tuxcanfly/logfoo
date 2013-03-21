from django.conf.urls import patterns, include, url

from foo.views import BarCreateView, BarListView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'logfoo.views.home', name='home'),
    url(r'^foo/', BarCreateView.as_view()),
    url(r'^', BarListView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
