from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('newblog/', views.NewblogView, name="newblog"),
    path('showblog/', views.ShowblogView, name="showblog"),
    path('delete/<id>/', views.DeleteView, name="delete"),
    path('update/<id>', views.UpdateView, name="update"),
    path('about/', views.AboutView, name="about"),
    path('contact/', views.ContactView, name="contact"),
    path('signup/', views.SignupView, name="signup"),
    path('signin/', views.SigninView, name="signin"),
    path('signout/', views.SignoutView, name="signout"),
    path('welcome/', views.WelcomeView, name="welcome"),

]

# Login Page User Details

# Nikhil123
# nik123456
