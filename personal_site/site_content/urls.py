from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('games', views.games, name='games'),
    path('games/fifteen', views.fifteen, name='fifteen'),
    path('games/twixt', views.twixt, name='twixt'),
    path('games/rubiks', views.rubiks, name='rubiks'),
    path('phil-theo', views.phil_theo, name='phil_theo'),
    path('services', views.services, name='services'),
]
