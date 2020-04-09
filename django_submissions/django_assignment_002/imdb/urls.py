from django.urls import path

from . import views

urlpatterns = [
    path('<int:actor_id1>/', views.index, name='index'),
]