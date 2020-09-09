from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Belonging(models.Model):
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


class ImageUpload(models.Model):
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image_name
