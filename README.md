Django Zongo
==============

Responsive presentations for Django using Bootstrap. 

A presentation is an image + html + css that match the Bootstrap breakpoints. You can provide a different presentation for every Bootstrap css breakpoints (+ 1 custom xxs breakpoint available).

Install
--------------

- Clone the repository
- Add `zongo,` to INSTALLED_APPS
- Make a `zongo` directory in `media`

In urls.py add the line:

	url(r'^zongo/', include('zongo.urls')),

Usage
--------------

Your app's models.py:

	from django.db import models
	from django.contrib.flatpages.models import FlatPage
	from zongo.models import Presentation
	
	class Page(FlatPage):
	    presentation=models.ForeignKey(Presentation, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Presentation') 

In the view.py:

- Get the presentation from the db in some way and put in a context object as `context['presentation']` (or use `context_object_name='presentation'` in generic class based views)

In the template:

	{% if presentation %}
		{% include 'zongo/main.html' %}
	{% endif %}

For a ready to use implementation check [django-alapage](https://github.com/synw/django-alapage)
