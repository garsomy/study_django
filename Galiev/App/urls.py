from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='Home', kwargs={'name': 'Daniil', 'age': '16', 'interests': 'Programming'}),
    path('about', views.about, name='About', kwargs={'city': 'Naberezhnye Chelny', 'functionality': 'Good', 'study': 'very love'}),
    path('contacts', views.contact, name='contacts', kwargs={'github': 'https://github.com/garsomy/study_django', 'phone': '89656198805'}),

]