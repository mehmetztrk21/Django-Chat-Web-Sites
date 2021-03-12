from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.urls import reverse


# Create your models here.
User = get_user_model()

class Chatt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    # konu=
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.message)

    def get_absolute_url(self):
	      return reverse('machine:all')


