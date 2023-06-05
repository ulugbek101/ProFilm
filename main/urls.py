from django.urls import path

from . import views


urlpatterns = [
     # http://localhost:8000/
     path('', views.index, name='home'),

     path('profile/', views.profile, name='profile'),

     # http://localhost:8000/delete/2/
     path('delete/<int:pk>/', views.delete, name='delete'),

     # https://localhost:8000/edit/2/
     path('edit/<int:pk>/', views.edit, name='edit'),

     # http://localhost:8000/film-detail/2/
     path('film-detail/<int:pk>/', views.detail, name='detail'),

     # http://localhost:8000/create-film/
     path('create-film/', views.create, name='create_film'),

     # http://localhost:8000/login/
     path('login/', views.signin, name='login'),

     # http://localhost:8000/register/
     path('register/', views.signup, name='register'),

     # https://localhost:8000/logout/
     path('logout/', views.signout, name='logout'),
]
