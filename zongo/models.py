# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class ZongoShow(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name=_(u'Title'))
    slug = models.SlugField(max_length=150, unique=True, default='', verbose_name=_(u'Id'), help_text=_(u"This field must not contain any spaces, special characters or capital letter"))
    image_lg = models.ImageField(upload_to='zongo', null=True, verbose_name=_(u'Image lg (1170px)'))
    image_md = models.ImageField(upload_to='zongo', blank=True, null=True, verbose_name=_(u'Image md (970px)'))
    image_sm = models.ImageField(upload_to='zongo', blank=True, null=True, verbose_name=_(u'Image sm (750px)'))
    image_xs = models.ImageField(upload_to='zongo', blank=True, null=True, verbose_name=_(u'Image xs (<750px)'))
    image_custom = models.ImageField(upload_to='zongo', blank=True, null=True, verbose_name=_(u'Image custom breakpoint'))
    html_lg = models.TextField(null=True, blank=True, verbose_name=_(u'Html lg'))
    html_md = models.TextField(null=True, blank=True, verbose_name=_(u'Html md'))
    html_sm = models.TextField(null=True, blank=True, verbose_name=_(u'Html sm'))
    html_xs = models.TextField(null=True, blank=True, verbose_name=_(u'Html xs'))
    html_custom = models.TextField(null=True, blank=True, verbose_name=_(u'Html custom breakpoint'))
    css_lg = models.TextField(null=True, blank=True, verbose_name=_(u'Css lg'))
    css_md = models.TextField(null=True, blank=True, verbose_name=_(u'Css md'))
    css_sm = models.TextField(null=True, blank=True, verbose_name=_(u'Css sm'))
    css_xs = models.TextField(null=True, blank=True, verbose_name=_(u'Css xs'))
    css_custom = models.TextField(null=True, blank=True, verbose_name=_(u'Css custom breakpoint'))
    custom_breakpoint = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_(u'Custom breakpoint'), help_text=_(u'Value for breakpoint in pixels'))

    
    class Meta:
        ordering = ('title',)
        verbose_name = _(u'Presentation')
        verbose_name_plural = _(u'Presentations')

    def __unicode__(self):
        return unicode(self.title)
    