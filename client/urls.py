from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='client-home'),
    path('login/', views.login, name='client-login'),
    path('logout/', views.logout, name='client-logout'),
    path('profile/<int:profile_id>/', views.view_profile, name='client-profile'),
    path('ad/new/', views.new, name='client-new'),
    path('ad/<int:ad_id>/', views.view_applicants, name='client-applicants'),
    path('ad/<int:ad_id>/accept/<int:user_id>/', views.accept, name='client-accept'),
    path('running/', views.running, name='client-running'),
    path('history/', views.history, name='client-history'),
    path('settings/', views.settings, name='client-settings'),
]
