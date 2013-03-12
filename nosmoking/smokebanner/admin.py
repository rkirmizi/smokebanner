from django.contrib import admin
from smokebanner.models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ['hours', 'cost', 'quantity', 'email']

admin.site.register(Banner, BannerAdmin)