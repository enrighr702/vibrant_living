from django.urls import path
from . import views
from django_distill import distill_path

urlpatterns = [
    distill_path('', views.index, name='index'),
    distill_path('about/', views.about, name='about'),
    distill_path('coaching/', views.coaching, name='coaching'),
    distill_path('contact/', views.contact, name='contact'),
    distill_path('testimonials/', views.testimonials, name='testimonials'),
]