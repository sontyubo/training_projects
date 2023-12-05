from django import forms
from django.contrib.auth.forms import UsernameField, AuthenticationForm

from .models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        }
    
    def clean_username(self):
        value = self.cleaned_data['username']
        min_length = 4
        if len(value) < min_length or value.isdigit():
            raise forms.ValidationError(f'{min_length}文字以上のアルファベットまたは記号で入力してください')
        return value
        
    def clean_password(self):
        value = self.cleaned_data['password']
        min_length = 4
        if len(value) < min_length or not value.isdigit():
            raise forms.ValidationError(f'{min_length}文字以上の数字で入力してください')
        return value
    
    def clean(self):
        super().clean()

class LoginForm(forms.Form):
    username = UsernameField(
    label='ユーザーネーム',
    max_length=255,
    widget=forms.TextInput(attrs={'placeholder': 'Username', 'autofocus': True, 'class': 'form-control'}),
    )

    password = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
    )