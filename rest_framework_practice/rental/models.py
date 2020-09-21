from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Friend(OwnerModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Belonging(OwnerModel):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s to %s" % (self.what, self.to_who)
