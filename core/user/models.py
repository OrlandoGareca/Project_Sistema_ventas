from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.
from appp.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    image = models.ImageField(upload_to='users/%d/%m/%Y', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL,self.image)
        return '{}{}'.format(STATIC_URL,'img/empty.png')
