from django.views.generic import ListView, DetailView
from smokebanner.models import Banner
from utils import banner
from nosmoking.settings import MEDIA_ROOT, MEDIA_URL


class BannersListView(ListView):
    model = Banner
    context_object_name = 'banner_list'
    template_name = 'list.html'


class BannerDetailView(DetailView):
    model = Banner
    template_name = 'detail.html'
    context_object_name = 'banner'

    def get_context_data(self, **kwargs):
        context = super(BannerDetailView, self).get_context_data(**kwargs)
        output_dir = MEDIA_ROOT
        output_file = 'hoba.png'
        nosmoke = banner.Banner(email='rkirmizi@gmail.com',
                                nosmoke_image='%s/nosmoke.png' % MEDIA_ROOT,
                                output_dir=output_dir,
                                output_file=output_file)
        nosmoke.banner()
        context['banner_image'] = '%s/%s' % (MEDIA_URL, output_file)
        # import pdb; pdb.set_trace();
        print self.get_object()
        return context
