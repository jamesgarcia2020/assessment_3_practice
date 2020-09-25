from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo/', views.TodoCreate.as_view(), name='add_todo'),
    path('<int:pk>/delete/', views.TodoDelete.as_view(), name='todos_delete'),
    path('<int:pk>/update/', views.TodoUpdate.as_view(), name='todos_update'),
]