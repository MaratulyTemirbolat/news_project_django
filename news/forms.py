import re

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

# from .models import Category
from .models import News


# Форма для отправки Писем
class ContactForm(forms.Form):  # noqa
    send_to = forms.CharField(label='Почта получателя',
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Тема',
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': 5}
                              ))
    captcha = CaptchaField()


class UserLoginForm(AuthenticationForm):  # noqa
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):  # noqa
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}),
                               help_text='Максимум 150 сивмолов')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(
                                    attrs={'class': 'form-control'}))

    class Meta:  # noqa
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    # title = forms.CharField(max_length = 150, label = 'Название ',widget=forms.TextInput(
    #     attrs={"class":'form-control'}
    # ))
    # content = forms.CharField(label = 'Текст ', required = False,widget = forms.Textarea(
    #     attrs={"class":'form-control','rows':5}
    # ))
    # is_published = forms.BooleanField(label = 'Опубликовано? ',initial = True)
    # category = forms.ModelChoiceField(empty_label = 'Выберите категорию',queryset = Category.objects.all(), label='Категория ',widget=forms.Select(
    #     attrs={"class":'form-control'}
    # ))
    
    # Для Формы связанной с моделью
    class Meta:  # Тут опишем как будет выглядеть наша Форма
        model = News  # Указываем с какой моделью будет связана наша форма
        #fields = '__all__' # Перечисляем поля, которые хотим видеть в данной форме. Если пишем __all__ то значит все поля
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
    # Я так понял, что работает только в Форме, потому что Админка пропускает это
    def clean_title(self):
        local_variable_title = self.cleaned_data['title']
        if(re.match(r'\d', local_variable_title)):
            raise ValidationError('Название не должно начинаться с цифры')
        return local_variable_title
