from django.views.generic import ListView, DetailView
from django.forms.models import model_to_dict
from smokebanner.models import Banner
from utils import banner
from nosmoking.settings import STATIC_ROOT, STATIC_URL
from datetime import datetime

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
        output_dir = STATIC_ROOT
        output_file = 'output.png'
        person = context.get('banner')
        kwargs_person = model_to_dict(person)
        quit_date = kwargs_person['quit_date'].date()
        today = datetime.today().date()
        total_days =  today - quit_date
        kwargs_person['quit_date'] = total_days
        kwargs_person.pop('id')

        nosmoke = banner.Banner(nosmoke_image='%s/nosmoke.png' % STATIC_ROOT,
                                output_dir=output_dir,
                                output_file=output_file,
                                **kwargs_person)
        nosmoke.banner()
        context['banner_image'] = '%s%s' %(STATIC_URL, output_file)
        return context
