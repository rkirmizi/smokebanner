from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from smokebanner.views import BannersListView, BannerDetailView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', BannersListView.as_view(), name='banner-list'),
    url(r'^banner/(?P<pk>\d+)/$', BannerDetailView.as_view(), name='banner-detail'),
	url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()