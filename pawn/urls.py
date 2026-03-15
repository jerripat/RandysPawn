from django.urls import path
from . import views

app_name = "pawn"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('guitars/', views.guitars, name='guitars')
]
