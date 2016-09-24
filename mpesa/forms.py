from mpesa.models import *
from django import forms

class SandBox_User(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password')

class Sandbox_Form(forms.ModelForm):
    class Meta:
        model = sandbox_user
        fields = ('email','phone','api_keys','api_secret','call_back_url','confirmation_code')
