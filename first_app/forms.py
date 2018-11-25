from django import forms
from django.core import validators
from first_app.models import User1
from first_app.models import UserProfileInfo
from django.contrib.auth.models import User

def check(value):
    if value[0] != 'z':
         raise forms.ValidationError("NOT QT TO Z")
 
class formname(forms.Form):
    name = forms.CharField(validators = [check])
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)
    bot = forms.CharField(widget = forms.HiddenInput, required = False)

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #         if (len(name) > 1):
    #             raise forms.ValidationError("hoooooooooooooooooo")
    #     return name
    

class newForm(forms.ModelForm):
    class Meta():
        model = User1
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfos(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_site',)