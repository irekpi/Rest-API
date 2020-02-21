from django.db import models
from django.conf import settings


class OwnerModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True


class Friend(models.Model):
    name = models.CharField(max_length=100)
    #email = models.EmailField(default='')


class Belonging(models.Model):
    name = models.CharField(max_length=100)


class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)

