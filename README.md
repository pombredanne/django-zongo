Django Allo
==============

Responsive presentations for Django using Bootstrap. 

A presentation is an image + html + css that match the Bootstrap breakpoints. You can provide a different presentation for every Bootrstrap css breakpoints (+ 1 custom breakpoint available).

Install
--------------

- Clone the repository
- Add *allo,* to INSTALLED_APPS

Usage
--------------

Your app's models.py:

	from django.db import models
	from django.contrib.flatpages.models import FlatPage
	from allo.models import FrontShow
	
	class Page(FlatPage):
	    presentation=models.ForeignKey(FrontShow, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Presentation') 

In the view.py:

- Get the presentation in the db in some way and put in a context object as *context['presentation']* (or use *context_object_name='presentation'* in generic cb views)

In the template:

	{% if presentation %}
		{% include 'allo/default.html' %}
	{% endif %}
