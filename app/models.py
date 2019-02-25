from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    photo = models.ImageField(upload_to='photos')
    bio = models.TextField()

    def __unicode__(self):
        return self.user.get_full_name()
