# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from zongo.models import Presentation, Screen
  

@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    save_as = True
    list_display= ('title','get_presentation_name','order')
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title','slug','presentation','order')
        }),
        ('Lg', {
            'classes': ('collapse',),
            'fields': ('image_lg','html_lg','css_lg')
        }),
        ('Md', {
            'classes': ('collapse',),
            'fields': ('image_md','html_md','css_md')
        }),
        ('Sm', {
            'classes': ('collapse',),
            'fields': ('image_sm','html_sm','css_sm')
        }),
        ('Xs', {
            'classes': ('collapse',),
            'fields': ('image_xs','html_xs','css_xs')
        }),
        ('Custom xxs', {
            'classes': ('collapse',),
            'fields': ('custom_breakpoint','image_xxs','html_xxs','css_xxs')
        })
    )
    
    def get_presentation_name(self, obj):
        return obj.presentation.title
    
    get_presentation_name.admin_order_field  = 'presentation'
    get_presentation_name.short_description = _(u'Presentation')

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    pass
    
