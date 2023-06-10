from django import forms
from .models import Profile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone', 'roll_num']
