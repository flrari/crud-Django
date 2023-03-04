from django.db import models

# Create your models here.
class Dipendenti(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    employee_code = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "dipendenti"