from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_trainer, name='register_trainer'),
    path('list/', views.trainer_list, name='trainer_list'),
    path('<int:id>/', views.register_trainer, name='trainer_update'),
    path('delete/<int:id>/', views.trainer_delete, name='trainer_delete'),
]
