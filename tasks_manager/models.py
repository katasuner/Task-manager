from django.db import models
from django.conf import settings

class Task(models.Model):
    class Status(models.IntegerChoices):
        NOT_COMPLETED = 0, "Активная"
        COMPLETED = 1, "Завершеная"

    class Priority(models.IntegerChoices):
        HIGH = 1, "Высокий"
        MEDIUM = 2, "Средний"
        LOW = 3, "Низкий"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='tasks',  verbose_name='Пользователь')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True)
    status = models.IntegerField(choices=Status.choices, default=Status.NOT_COMPLETED)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

