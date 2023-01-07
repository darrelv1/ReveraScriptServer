from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Report(models.Model):
    #Reference for learning: Field types for Django Models (model field reference)
    title = models.CharField(max_length=50)
    entityID = models.IntegerField(
        validators=[MinLengthValidator(2),MaxLengthValidator(5)])
    creator = models.CharField(null=True, max_length=100)
    is_Current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.entityID})"