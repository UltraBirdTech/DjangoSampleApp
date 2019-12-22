from django import forms

class HelloSearchForm(forms.Form):
    id = forms.IntegerField(label='ID')

class HelloCreateForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender', required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')
