from django.contrib.auth.models import AbstractUser, User
from django.db import models


class User(AbstractUser):
    pass

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    date = models.DateField(u'date', auto_now=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'