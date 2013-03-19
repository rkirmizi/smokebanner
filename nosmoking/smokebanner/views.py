from django.views.generic import ListView, DetailView
from django.forms.models import model_to_dict
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
        person = context.get('banner')
        kwargs_person = model_to_dict(person)
        kwargs_person['email'] = 'rkirmizi@gmail.com'
        kwargs_person.pop('id')
        nosmoke = banner.Banner(nosmoke_image='%s/nosmoke.png' % MEDIA_ROOT,
                                output_dir=output_dir,
                                output_file=output_file,
                                **kwargs_person)
        nosmoke.banner()
        context['banner_image'] = '%s/%s' % (MEDIA_URL, output_file)
        return context
