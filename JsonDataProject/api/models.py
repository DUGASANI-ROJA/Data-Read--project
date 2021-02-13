from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id = models.CharField(unique=True, max_length=20)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)

    def __str__(self):
        return str(self.real_name)+" "+str(self.employee_id)


class ActivityPeriods(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.start_time)