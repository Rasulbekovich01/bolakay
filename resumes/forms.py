from django.forms import ModelForm
from resumes.models import Resume

class ResumeForm(ModelForm):
    class Meta:
        model= Resume
        fields= ['first_name', 'last_name', 'email', 'birth_date', 'job', 'experience']


class AddResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields= '__all__'