# Create your models here.


# deklaracija
from django.conf import settings
from django.db import models
from django.utils import timezone


# klasa objekta strank
class Post(models.Model):
    stranka = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    podjetje = models.CharField(max_length=20)
    reference = models.TextField()
    email = models.EmailField()
    datum_ponudbe = models.DateTimeField(default=timezone.now)
    datum_knj_ponudbe = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.datum_ponudbe = timezone.now()
        self.save()

    def __str__(self):
        return self.podjetje


# end
