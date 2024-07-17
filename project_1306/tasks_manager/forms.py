from django.forms import ModelForm
from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority']
        labels = {
            'title': 'Название задачи',
            'description': 'Подробное описание',
            'due_date': 'Дата выполнения',
            'status': 'Текущий статус',
            'priority': 'Приоритет задачи'
        }
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)
        super().__init__(*args, **kwargs)
        if is_update:
            for field in self.fields.values():
                field.required = False


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        