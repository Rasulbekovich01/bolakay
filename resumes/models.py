from django.db import models

# Create your moc

class Resume(models.Model):
    first_name =models.CharField(max_length=225, null=True)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField(max_length=100)
    job = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

