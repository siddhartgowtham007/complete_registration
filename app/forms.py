from app.models import *
from django import forms

class userforms(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}


class profileforms(forms.ModelForm):
    class Meta:
        model=profile
        fields=['adress','profile_pic']
