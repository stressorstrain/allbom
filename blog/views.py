from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = '/home/guibax/allbom/blog/templates/blog/front_page.html'

class SingIn(TemplateView):
    template_name = '/home/guibax/allbom/blog/templates/blog/sing_page.html'