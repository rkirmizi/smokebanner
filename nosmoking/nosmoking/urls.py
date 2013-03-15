from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from smokebanner.views import BannersListView, BannerDetailView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', BannersListView.as_view(), name='banner-list'),
    url(r'^banner/(?P<pk>\d+)/$', BannerDetailView.as_view(), name='banner-detail'),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
