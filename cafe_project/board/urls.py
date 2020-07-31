
from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.board_read, name = 'board_read'),
    path('create/', views.board_create, name = 'board_create'),
    path('read/<int:pk>', views.board_read_one, name = 'board_read_one'),
    path('update/<int:pk>',views.update_board, name = 'update_board'), 
    path('delete/<int:pk>',views.delete_board, name = 'delete'),
    path('pre_update/<int:pk>',views.pre_update, name ='pre_update'),
]