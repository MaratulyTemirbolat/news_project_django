from django import forms

from .models import Category
from .models import News
import re
from django.core.exceptions import ValidationError

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
    class Meta: # Тут опишем как будет выглядеть наша Форма
        model = News  # Указываем с какой моделью будет связана наша форма
        #fields = '__all__' # Перечисляем поля, которые хотим видеть в данной форме. Если пишем __all__ то значит все поля
        fields = ['title','content','is_published','category']
        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control'}),
            'content':forms.Textarea(attrs = {'class':'form-control','rows':5}),
            'category':forms.Select(attrs = {'class':'form-control'})
        }
    # Я так понял, что работает только в Форме, потому что Админка пропускает это
    def clean_title(self):
        local_variable_title = self.cleaned_data['title']
        if(re.match(r'\d',local_variable_title)):
            raise ValidationError('Название не должно начинаться с цифры')
        return local_variable_title
