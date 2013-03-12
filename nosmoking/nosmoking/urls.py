from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from smokebanner.views import BannersList, BannerDetail
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nosmoking.views.home', name='home'),
    url(r'^$', BannersList.as_view(), name='banner-list'),

    url(r'^banner/(?P<pk>[-_\w]+)/$', BannerDetail.as_view(), name='banner-detail'),

	# (r'^banners/detail', BannerDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
