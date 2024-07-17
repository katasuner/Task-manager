from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView, RegisterView, main_page
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', main_page, name='home'),
    path('tasks_list/', TaskListView.as_view(), name='tasks_list'),
    path('task_create/', TaskCreateView.as_view(), name='task_create'),
    path('task_update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('login/', LoginView.as_view(template_name='tasks_manager/login.html', next_page='tasks_list'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]