# -*- coding: utf-8 -*-

from django.contrib import admin
from zongo.models import ZongoShow

@admin.register(ZongoShow)
class ZongoShowAdmin(admin.ModelAdmin):
    list_display= ('title','slug',)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title','slug',)
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
            'fields': ('custom_breakpoint','image_custom','html_custom','css_custom')
        })
    )
