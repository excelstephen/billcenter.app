from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'First Name'
        }))
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'Last Name'
        }))
    email = forms.EmailField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'Email'
        }))

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        
        if email and CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters.")
        return password

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = None
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = None





class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': '', 
            'placeholder': 'Enter your email'
        }),
        label=""
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': '', 
            'placeholder': 'Enter your password'
        }),
        label=""
    )