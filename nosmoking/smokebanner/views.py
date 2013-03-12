from django.views.generic import ListView, DetailView
from smokebanner.models import Banner

class BannersList(ListView):
    model = Banner
    context_object_name = 'banner_list'
    template_name = 'list.html'

class BannerDetail(DetailView):
    model = Banner
    template_name = 'detail.html'
    context_object_name = 'banner'