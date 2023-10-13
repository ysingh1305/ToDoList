from django.urls import path 
from .views import deleteView, taskList, taskDetail, taskCreate, taskUpdate, deleteView, customLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', customLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('register/', RegisterPage.as_view(), name = 'register'),
    path('', taskList.as_view(), name = 'tasks'),
    path('task/<int:pk>/', taskDetail.as_view(), name = 'task'),
    path('task-create/', taskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', taskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', deleteView.as_view(), name = 'task-delete'),


]