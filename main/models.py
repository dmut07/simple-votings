import datetime

from django.contrib.auth.models import User
from django.db import models
from django import forms

class Profile(models.Model):
    login = models.CharField(max_length=20, blank=False, default='Login')
    user = models.ForeignKey(User, models.CASCADE, default='user')  # Он хранит пароль/логин и прочее


class Vote(models.Model):
    """
    Модель голосования

    title - название
    description - описание
    # public_datetime - дата и время публикации
    # mode - режим голосования
    # - 0 - дискретный выбор (да/нет)
    # - 1 - Один из вариантов (Options)
    # - 2 - Много вариантов (Options)
    author - профиль пользователя, создавшего голосование
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=255, null=True, default='Anonim')


class Option(models.Model):
    """
    Модель варианта ответа (Один из или много)

    name - название
    count - кол-во голосов
    vote - голосование, к которому прикреплен данный вариант
    """
    name = models.CharField(max_length=64)
    count = models.IntegerField(default=0)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)

# TODO: Как понять, что пользователь уже проголосовал?
    pass
