from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12, unique=False)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    isCompleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'

    def __str__(self):
        return self.title
