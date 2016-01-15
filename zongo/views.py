# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.utils.translation import ugettext_lazy as _
from zongo.models import Presentation, Screen

def presentationView(request, presentation_slug):
    if request.is_ajax():
        try:
            presentation=get_object_or_404(Presentation.objects.prefetch_related('screen'), slug=presentation_slug)
            screens=presentation.screen.all()
            num_screens = len(screens)
            if num_screens == 0:
                return HttpResponse('')
            return render_to_response('zongo/default.html',
                               {'presentation':presentation, 
                                'zscreen':screens[0],
                                #'num_zscreens':num_screens,
                                },
                               content_type="application/xhtml+xml"
                               )
        except:
            return HttpResponse(_(u"Error"))
    else:
        raise Http404
    
def nextScreenView(request, presentation_slug, screen_slug):
    if request.is_ajax():
        try:
            presentation=get_object_or_404(Presentation.objects.prefetch_related('screen'), slug=presentation_slug)
            screen=presentation.screen.get(slug=screen_slug)
            return render_to_response('zongo/default.html',
                               {'presentation':presentation, 
                                'zscreen':screen,
                                },
                               content_type="application/xhtml+xml"
                               )
        except:
            return HttpResponse(_(u"Error"))
    else:
        raise Http404