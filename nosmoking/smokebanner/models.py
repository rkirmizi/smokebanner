from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site


class Banner(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    email = models.EmailField(max_length=75)
    quit_date = models.DateTimeField()
    cost_per_package = models.IntegerField(max_length=5)
    daily_quantity = models.IntegerField(max_length=5)
    first_row = models.CharField(max_length=100)
    second_row = models.CharField(max_length=100)
    footer = models.CharField(max_length=100, null=True)
    site = models.ForeignKey(Site)


    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')
        get_latest_by = 'id'

    def __unicode__(self):
        return u'%s %s - %s' % (self.first_name, self.last_name, self.email)

    def get_absolute_url(self):
        return "/banner/%i/" % (self.id)
