# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Presentation(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name=_(u'Title'))
    slug = models.SlugField(max_length=150, unique=True, verbose_name=_(u'Id'), help_text=_(u"This field must not contain any spaces, special characters or capital letter"))
    html_before = models.TextField(null=True, blank=True, verbose_name=_(u'Html before'))
    html_after = models.TextField(null=True, blank=True, verbose_name=_(u'Html after'))
    
    class Meta:
        ordering = ('title',)
        verbose_name = _(u'Presentation')
        verbose_name_plural = _(u'Presentations')

    def __unicode__(self):
        return unicode(self.title)


class Screen(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name=_(u'Title'))
    slug = models.SlugField(max_length=150, unique=True, default='', verbose_name=_(u'Id'), help_text=_(u"This field must not contain any spaces, special characters or capital letter"))
    presentation = models.ForeignKey(Presentation, null=True, related_name='screen', verbose_name=_(u'Presentation'))
    link = models.URLField(null=True, blank=True, verbose_name=_(u'Link on image'))
    order = models.PositiveSmallIntegerField(null=True, verbose_name=_(u'Order'))
    #~ images
    image_lg = models.ImageField(upload_to='zongo', null=True, verbose_name=_(u'Image lg (1170px)'))
    image_md = models.ImageField(upload_to='zongo', blank=True, null=True, verbose_name=_(u'Image md (970px)'))
    image_sm = models.ImageField(upload_to='zongo', blank=True, null=True, verbose_name=_(u'Image sm (750px)'))
    image_xs = models.ImageField(upload_to='zongo', blank=True, null=True, verbose_name=_(u'Image xs (<750px)'))
    image_xxs = models.ImageField(upload_to='zongo', blank=True, null=True, verbose_name=_(u'Image xxs'))
    #~ html
    html_lg = models.TextField(null=True, blank=True, verbose_name=_(u'Html lg'))
    html_md = models.TextField(null=True, blank=True, verbose_name=_(u'Html md'))
    html_sm = models.TextField(null=True, blank=True, verbose_name=_(u'Html sm'))
    html_xs = models.TextField(null=True, blank=True, verbose_name=_(u'Html xs'))
    html_xxs = models.TextField(null=True, blank=True, verbose_name=_(u'Html xxl'))
    #~ css
    css_lg = models.TextField(null=True, blank=True, verbose_name=_(u'Css lg'), help_text=_(u'Use the "lg_bp" css id to select the html in this block'))
    css_md = models.TextField(null=True, blank=True, verbose_name=_(u'Css md'), help_text=_(u'Use the "md_bp" css id to select the html in this block'))
    css_sm = models.TextField(null=True, blank=True, verbose_name=_(u'Css sm'), help_text=_(u'Use the "sm_bp" css id to select the html in this block'))
    css_xs = models.TextField(null=True, blank=True, verbose_name=_(u'Css xs'), help_text=_(u'Use the "xs_bp" css id to select the html in this block'))
    css_xxs = models.TextField(null=True, blank=True, verbose_name=_(u'Css xxs'), help_text=_(u'Use the "xxs_bp" css id to select the html in this block'))
    custom_breakpoint = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_(u'Custom xxs breakpoint'), help_text=_(u'Value for breakpoint in pixels'))

    
    class Meta:
        ordering = ('order','title')
        order_with_respect_to = 'presentation'
        verbose_name = _(u'Screen')
        verbose_name_plural = _(u'Screens')

    def __unicode__(self):
        return unicode(self.title)
    