from django.conf.urls import patterns, url
from zongo.views import presentationView, nextScreenView


urlpatterns = patterns('',
    url(r'^(?P<presentation_slug>[-_\w]+)/(?P<screen_slug>[-_\w]+)/$', nextScreenView, name='presentation-home'),
    url(r'^(?P<presentation_slug>[-_\w]+)/$', presentationView, name='presentation-home'),
)