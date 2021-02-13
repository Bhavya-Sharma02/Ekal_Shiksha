from django.shortcuts import render

from django.http import HttpResponse
from .models import student
from .forms import abc
from django.views.generic import CreateView

class hm(CreateView):
    model = student
    form_class = abc
    template_name = 'Index_copy.html'

class class_6th(CreateView):
    model = student
    form_class = abc
    template_name = 'class_6th.html'

class class_7th(CreateView):
    model = student
    form_class = abc
    template_name = 'class_7th.html'

class class_8th(CreateView):
    model = student
    form_class = abc
    template_name = 'class_8th.html'

class class_9th(CreateView):
    model = student
    form_class = abc
    template_name = 'class_9th.html'


class class_10th(CreateView):
    model = student
    form_class = abc
    template_name = 'class_10.html'

class Science_11th(CreateView):
    model = student
    form_class = abc
    template_name = 'science_11.html'
class Science_12th(CreateView):
    model = student
    form_class = abc
    template_name = 'science_12.html'
class Doubts(CreateView):
    model = student
    form_class = abc
    template_name = 'Doubts.html'
class MicroCourse9th(CreateView):
    model = student
    form_class = abc
    template_name = 'MicroCourse6th.html'
# def c6(response):
#     return render(response,'class_6th.html')
# def c7(response):
#     return render(response,'class_7th.html')
