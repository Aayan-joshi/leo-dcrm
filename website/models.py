from django.db import models

# Create your models here.
class Member(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    address =models.CharField(max_length=100)
    institution = models.CharField(max_length=200, default="")
    payment_method = models.CharField(max_length=40, default="")
    blood_group =models.CharField(max_length=50)
    date_of_birth =models.DateField(max_length=50)
    contact =models.CharField(max_length=15)
    email =models.CharField(max_length=150)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")