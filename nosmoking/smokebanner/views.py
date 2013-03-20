from django.views.generic import ListView, DetailView
from django.forms.models import model_to_dict
from smokebanner.models import Banner
from utils import banner
from nosmoking.settings import STATIC_ROOT, STATICFILES_DIRS
from datetime import datetime
from django.contrib.sites.models import Site


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
        output_dir = STATICFILES_DIRS[0]
        output_file = 'output.png'
        person = context.get('banner')
        kwargs_person = model_to_dict(person)
        quit_date = kwargs_person['quit_date'].date()
        today = datetime.today().date()
        total_days =  today - quit_date
        kwargs_person['quit_date'] = total_days.days
        kwargs_person.pop('id')
        context['full_image_path'] = 'http://%s%s' % (Site.objects.get_current().domain, self.request.get_full_path())

        nosmoke = banner.Banner(nosmoke_image='%s/nosmoke.png' % STATIC_ROOT,
                                output_dir=output_dir,
                                output_file=output_file,
                                **kwargs_person)
        nosmoke.banner()
        return context