from django.contrib.auth.models import User
from django.db import models

class Ufsstars(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    art = models.ForeignKey('Art', on_delete=models.PROTECT, null=True)
    weight = models.ForeignKey('Weight', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Art(models.Model):
    type_of_art = models.CharField(max_length=40, db_index=True)
    # wrestling = models.CharField(max_length=30, db_index=True)
    # box = models.CharField(max_length=30)
    # kickboxing = models.CharField(max_length=30)
    # BJJ = models.CharField(max_length=30)
    # MMA = models.CharField(max_length=30)
    def __str__(self):
        return self.type_of_art

class Weight(models.Model):
    type_of_weight = models.CharField(max_length=30, db_index=True)
    # flyweight = models.CharField()
    # bantamweight = models.CharField()
    # featherweight = models.CharField()
    # lightweight = models.CharField()
    # welterweight = models.CharField()
    # middleweight = models.CharField()
    # light_heavyweight = models.CharField()
    # heavyweight = models.CharField()
    def __str__(self):
        return self.type_of_weight
