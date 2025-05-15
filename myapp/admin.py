from django.contrib import admin
from .models import Contact, Index_Slider, Why_Choose_Us, About_Container,Trainers_Container,Info_Section,Shop,Blog

class contact_filter(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','created_at')

class slider_filter(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

class why_choose_us_filter(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')

class about_container_filter(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')

class trainers_container_filter(admin.ModelAdmin):
    list_display = ('trainer_name', 'created_at', 'updated_at')

class info_section(admin.ModelAdmin):
    list_display = ('item_name', 'created_at', 'updated_at')

class shop_filter(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'created_at', 'updated_at')

class blog_filter(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')


admin.site.register(Contact, contact_filter)
admin.site.register(Index_Slider, slider_filter)
admin.site.register(Why_Choose_Us,why_choose_us_filter)
admin.site.register(About_Container, about_container_filter)
admin.site.register(Trainers_Container, trainers_container_filter)
admin.site.register(Info_Section, info_section)
admin.site.register(Shop,shop_filter)
admin.site.register(Blog, blog_filter)