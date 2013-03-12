from django.db import models
from django.utils.translation import ugettext as _

class Banner(models.Model):
    hours = models.DateTimeField(auto_now=True)
    cost = models.IntegerField(max_length=5)
    quantity = models.IntegerField(max_length=5)
    email = models.EmailField(max_length=75)

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')

    def __unicode__(self):
        return u'%s' %(self.email)

    # def save(self):
    #     pass

    # @models.permalink
    def get_absolute_url(self):
    	return "/banner/%i/" % self.id

    # TODO: Defne custom methods here

    