from django import forms

class HelloForm(forms.Form):
    print(type(forms))
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')

