from django.views.generic import ListView, DetailView
from smokebanner.models import Banner
from utils import banner
from nosmoking.settings import MEDIA_ROOT

class BannersList(ListView):
    model = Banner
    context_object_name = 'banner_list'
    template_name = 'list.html'

class BannerDetail(DetailView):
    model = Banner
    template_name = 'detail.html'
    context_object_name = 'banner'

    def get_context_data(self, **kwargs):
		context = super(BannerDetail, self).get_context_data(**kwargs)
		nosmoke = banner.Banner(email='rkirmizi@gmail.com', nosmoke_image='%s/nosmoke.png' %MEDIA_ROOT)
		context['nosmoke_image'] = nosmoke
		return context