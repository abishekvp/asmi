from django import forms
from .models import File

class Form(forms.ModelForm):
    class Meta:
        model=File
        fields=('file','prompt')
        
class MyForm(forms.Form):
    name = forms.CharField(label='Prompt')
    file = forms.FileField(label='File')