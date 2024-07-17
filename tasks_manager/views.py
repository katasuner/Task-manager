from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView
from .models import Task
from .forms import TaskForm, UserRegisterForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin



def main_page(request):
    return render(request, 'tasks_manager/main_page.html')


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks_manager/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'id')
        order = self.request.GET.get('order', 'asc')
        if order == 'desc':
            sort = f'-{sort}'
        return queryset.filter(user=self.request.user).order_by(sort)



class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks_manager/task_create.html'
    success_url = reverse_lazy('tasks_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['is_update'] = False  
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks_manager/task_delete.html'
    success_url = reverse_lazy('tasks_list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks_manager/task_update.html'
    success_url = reverse_lazy('tasks_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['is_update'] = True  
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            'title': self.object.title,
            'description': self.object.description,
            'due_date': self.object.due_date,
            'status': self.object.status,
            'priority': self.object.priority,
        })
        return initial

    def form_valid(self, form):
        return super().form_valid(form)



class RegisterView(FormView):
    template_name = 'tasks_manager/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

