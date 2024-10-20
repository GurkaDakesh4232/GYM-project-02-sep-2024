from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handlelogout"),
    path('contact',views.contact,name="contact"),
    path('enroll',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),
    path('service',views.service,name="service")


]
