from django.contrib import admin
from smokebanner.models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'quit_date', 'cost_per_package', 'daily_quantity']
    
admin.site.register(Banner, BannerAdmin)