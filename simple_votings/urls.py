from django.contrib import admin
from django.urls import path

from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('votes/', views.votes, name='votes'),
    path('vote_form/', views.vote_create_page, name='vote_form'),
    path('vote/<int:_id>', views.voting_page, name="voting"),
    path('time/', views.time_page, name='time'),
    path('registration/', views.registration_page, name='registration'),
    path('login/', views.login_page, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
