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



    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(BannerDetail, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['banner_list'] = Banner.objects.all()
    #     return context