from django import forms
from .models import student

class abc(forms.ModelForm):
    class Meta:
        model= student
        fields= ('Name','Email','Number','Class','Course','Information')
        labels = {
            'Information':'What you want to enquire for???',
        }

        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control', 'required': True}),
            'Email': forms.EmailInput(attrs={'class':'form-control', 'required': True}),
            'Number': forms.TextInput(attrs={'class':'form-control','required': True,}),
            'Class':forms.TextInput(attrs={'class':'form-control', 'required': True}),
            'Course':forms.TextInput(attrs={'class':'form-control', 'required': True}),
            'Information':forms.Textarea(attrs={'class':'form-control', 'required': True}),
        }
