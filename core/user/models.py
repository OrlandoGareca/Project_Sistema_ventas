from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.
from django.forms import model_to_dict

from appp.settings import MEDIA_URL, STATIC_URL



class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password','user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item

    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         self.set_password(self.password)
    #     else:
    #         user = User.objects.get(pk=self.pk)
    #         if user.password != self.password:
    #             self.set_password(self.password)
    #     super().save( *args, **kwargs)

