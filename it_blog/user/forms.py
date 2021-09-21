from django import forms
from django.forms.widgets import TextInput


class UserSignIn(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                "id": "name",
                "class": "form-control",
                "placeholder": 'Name',
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'User name'",
            }
        )

    )
    phone = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField()
    repeat_password = forms.CharField()
    is_agree = forms.BooleanField()