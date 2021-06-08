from django import forms

class SimpleForm(forms.Form):
    name= forms.CharField()
    description= forms.CharField (widget=forms.Textarea)