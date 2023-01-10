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


class ReportStats(models.Model):
    #Triggered For Every Report Printed
    Date = models.DateField(default=False)
    TransID = models.BigIntegerField(default=False)
    Accountant = models.CharField(max_length=50)
    ReportName = models.CharField(max_length=100)
    ReportType =models.CharField(max_length = 100)
    #Report Size
    ReportLen = models.IntegerField(default=False)
    ReportWidth = models.IntegerField(default=False)
    ReportWidth = models.IntegerField(default=False)
    ReportTotal = models.IntegerField(default=False)
    ReportAverage = models.IntegerField(default=False)
    ReportStdDevation = models.IntegerField(default=False)
 
    
    def __str__(self): 
        return f"{self.Users}, {self.ReportType}, {self.ReportName}, {self.ReportLen}"

class Accountant(models.Model): 
    #Store for retrieve of user account data
    AccountantName = models.CharField(max_length=50)

    
class PM(models.Model):
    #One-to-many relationship with
    name = models.CharField(max_length=100)
    User = models.ForeignKey(Accountant, on_delete=models.CASCADE)






    