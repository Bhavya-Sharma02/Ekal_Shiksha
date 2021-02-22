from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *
urlpatterns = [
    path('', hm.as_view(), name='index'),
    path('6th/', class_6th.as_view(), name='6th'),
    path('7th/', class_7th.as_view(), name='7th'),
    path('8th/', class_8th.as_view(), name='8th'),
    path('9th/', class_9th.as_view(), name='9th'),
    path('10th/', class_10th.as_view(), name='10th'),
    path('Doubts/', Doubts.as_view(), name='Doubts'),
    path('11th_Science/', Science_11th.as_view(), name='11th_Science'),
    path('12th_Science/', Science_12th.as_view(), name='12th_Science'),
    path('MicroCourse9th/', MicroCourse9th.as_view(), name='MicroCourse9th'),
    path('MicroCourse10th/', MicroCourse10th.as_view(), name='MicroCourse10th'),
    path('12th_Commerce/', Commerce_12th.as_view(), name='12th_Commerce'),
    path('11th_Commerce/', Commerce_11th.as_view(), name='11th_Commerce'),
    path('11th_Humanities/', Humanities_11th.as_view(), name='11th_Humanities'),
    path('12th_Humanities/', Humanities_12th.as_view(), name='12th_Humanities'),
    # path('class_6th',views.c6),
    # path('class_7th',views.c7),

]
