from django import forms
from.models import Friend

class HelloSearchForm(forms.Form):
    id = forms.IntegerField(label='ID')

class FriendCreateForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']

class HelloCreateForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender', required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')
