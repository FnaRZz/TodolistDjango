from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyTasks(models.Model):
    task_name = models.CharField('Название задачи',max_length=150,default='NoNameTask')
    task_desc = models.CharField('Описание задачи',max_length=512,default='No descriptions')
    task_complited = models.BooleanField('Задача выполнена',default=False)
    task_by_user = models.ForeignKey(User,on_delete=models.PROTECT)
    def __str__(self):
        return self.task_name
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'