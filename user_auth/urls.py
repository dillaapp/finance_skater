from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register_user/', views.register_user, name="register_user")

]
