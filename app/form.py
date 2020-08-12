from django import forms
from .models import *

class stu_form(forms.Form):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'style':'width: 100%; height: 45px;',
                                                                        'class':'form-control',
                                                                        'placeholder' : "Enter Name"
                                                                       }))