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
        person = context.get('banner')
        nosmoke = banner.Banner(first_name=person.first_name,
                                last_name=person.last_name,
                                email='rkirmizi@gmail.com',
                                quit_date=person.quit_date,
                                cost_per_package=person.cost_per_package,
                                daily_quantity=person.daily_quantity,
                                first_row=person.first_row,
                                second_row=person.second_row,
                                footer=person.footer,
                                nosmoke_image='%s/nosmoke.png' % MEDIA_ROOT,
                                output_dir=output_dir,
                                output_file=output_file)
        nosmoke.banner()
        context['banner_image'] = '%s/%s' % (MEDIA_URL, output_file)
        return context
