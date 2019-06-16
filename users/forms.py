from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(initial='', widget=forms.PasswordInput())
    repassword = forms.CharField(
        initial='', label='Confirm password',widget=forms.PasswordInput()
    )
    class Meta:
        model = User
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
