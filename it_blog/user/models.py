import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.utils.deconstruct import deconstructible




@deconstructible
class _Phone_validator:
    _pattern = re.compile(
    r"^^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    )
    def __call__(self, value):
        if not self._pattern.match(value):
            raise ValidationError("{!r}, Value is not phone number".format(value))




class User(AbstractUser):
    phone = models.CharField(
    max_length=20,
    validators=[_Phone_validator()],
    null = True,
    verbose_name="User")

    def send_sms(self, message):
        ...


    def __str__(self) -> str:
        return self.username


    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

@receiver(pre_save, sender=User)
def hash_passwd(sender, instance, **kwargs):
    if (instance.id is None) or (sender.objects.get(id=instance.id).password != instance.password):
        instance.set_password(instance.password)
    


