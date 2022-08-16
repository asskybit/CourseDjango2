from django.urls import path

from . import views

urlpatterns = [

    path('<slug:post_name>/', views.PostView.as_view(), name='post'),
    path('', views.HomeView.as_view()),
]
