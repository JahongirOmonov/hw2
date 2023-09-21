from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Kasblar(AbstractUser):
    Vakillar = (
        (3,'Yurist'),
        (2, 'Coder'),
        (1, 'Direktor')
    )

    vazifalari = models.PositiveIntegerField(choices=Vakillar, default=1)
