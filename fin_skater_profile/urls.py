from django.urls import path, include
from . import views


app_name = 'fin_skater_profile'
urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name="about_us"),
]
