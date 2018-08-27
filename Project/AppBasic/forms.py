from django.contrib.auth.models import User
from django import forms
from .models import UserAccount,DataModel

class UserAccountInfo(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(),min_length=8)
    class Meta():
        model = User
        fields = ('username','email','first_name','last_name','password')

class UAExtraInfo(forms.ModelForm):
    class Meta():
        model = UserAccount
        fields = ('Your_Website','Profile_Pic')

class postform(forms.ModelForm):
    Description = forms.CharField(widget = forms.Textarea)
    class Meta():
        model = DataModel
        fields = '__all__'