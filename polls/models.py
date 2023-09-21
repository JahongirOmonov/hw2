from django.db import models

# Create your models here.

class Korxona(models.Model):
    info = models.CharField(default='', max_length=202)
    detail = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.info
    

