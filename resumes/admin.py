from django.contrib import admin
from .models import Resume

# Register your models here.


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
        list_display=('last_name', 'first_name', 'email', 'birth_date', 'job', 'experience' )