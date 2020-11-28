from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.saveData, name='save'),
    path('delete/', views.deleteData, name='delete'),
    path('edit/', views.editData, name='edit'),
]
