from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from authserver.metadata import MetaData


class User(AbstractUser,MetaData):
    img = models.FileField(upload_to='static/media/', verbose_name='Change Profile Image')
    USERNAME_FIELD = "email"


    class Meta:
        db_table = "users"