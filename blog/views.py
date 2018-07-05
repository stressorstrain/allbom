from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = '/home/guibax/allbom/django/blog/templates/blog/front_page.html'

class AboutPageView(TemplateView):
    template_name = '/home/guibax/allbom/django/django/blog/templates/blog/sing_page.html'