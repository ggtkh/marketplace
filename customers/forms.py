from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS классы к каждому полю
        self.fields['username'].widget.attrs.update({'class': 'form-input',
                                                    'placeholder': "І'мя користувача"})
        self.fields['email'].widget.attrs.update({'class': 'form-input', 
                                                  'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 
                                                      'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 
                                                      'placeholder': 'Повторіть пароль'})
        
        self.fields['username'].help_text = "Не більше 150 символів. Лише букви, цифри та @/./+/-/_"
        self.fields['password2'].help_text = "Повторіть пароль для підтвердження."

        self.fields['username'].label = "Ім'я користувача"
        self.fields['email'].label = "Електронна адреса"
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Підтвердження пароля"

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input',
                                                    'placeholder': "І'мя користувача"})
        self.fields['password'].widget.attrs.update({'class': 'form-input', 
                                                     'placeholder': 'Пароль'})
        
        self.fields['username'].label = "Ім'я користувача"
        self.fields['password'].label = "Пароль"