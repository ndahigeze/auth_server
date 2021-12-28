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

    def find_by_email(email):

        try:
            return User.objects.get(email=email, deleted_status=False)
        except Exception as e:
            return None

    def find_by_uuid(uuid):
        try:
            return User.objects.get(uuid=uuid, deleted_status=False)
        except Exception as e:
            return None

