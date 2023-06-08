from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('', views.registerPage, name = "register"),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),

]
