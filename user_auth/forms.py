from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
# from .models import CustomUser as User

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('email', 'username')

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(username=username, email=email, password=password)
            if user is None or not user.is_active:
                raise forms.ValidationError('Invalid email, username, or password')
        return cleaned_data
