from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_musician, name='add_musician'),
    path('delete/<int:id>', views.delete_musician, name='delete_musician'),

]
