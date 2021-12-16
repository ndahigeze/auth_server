from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from encrypted_id.models import EncryptedIDModel

from authserver.metadata import MetaData


class User(AbstractUser,MetaData,EncryptedIDModel):
    img = models.FileField(upload_to='static/media/', verbose_name='Change Profile Image')
    email = models.CharField(max_length=255, blank=False,null=False, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    class Meta:
        db_table = "users"