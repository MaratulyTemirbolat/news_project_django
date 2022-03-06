# from hashlib import new
# from unicodedata import category
# from django import template
# from django.shortcuts import render
# from matplotlib.style import context
# from sympy import N, Ne
# from django.shortcuts import get_object_or_404
# from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView
# Данный класс предназначен для работы со списками.
# Задача его, вернуть список.
# Помогает вернуть список объектов для какой-то страницы
from django.views.generic import DetailView
# Данный класс предназнен для конкретной новости (Экземпляра объекта)
from django.views.generic import CreateView
# Данный класс предназначен для создание новости
# (Экземпляра объекат), работа с Формой
from django.contrib.auth.mixins import LoginRequiredMixin
# Используем для тех классов, для которых надо ограничить доступ
from django.core.paginator import Paginator

from .models import News
from .models import Category

from .forms import NewsForm

# from django.urls import reverse_lazy 
# # Делает тоже самое, что и reverse, но он срабатывает 
# только тогда, когда до него дойдет очередь. 
# Т.е когда все будет только работать, все маршруты подгрузятся, 
# то reverse_lazy построит ссылку


def test(request):
    objects = ['john1', 'paul2',
               'george3', 'ringo4',
               'john5', 'paul6',
               'george7', ]
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    # Если нет page в url адресе, то будет присвоена 1 по умолчанию
    page_objects = paginator.get_page(page_num)
    # Получем объекты заданной страницы
    return render(request, 'news/test.html', {'page_obj': page_objects})


class HomeNews(ListView):
    # Есть аттрибуты, которые мы должны переобределить.
    model = News
    # Модель, из который мы хотим получить список.
    # Аналог news = News.objects.all()
    template_name = 'news/home_news_list.html'
    # Путь к нужному нам шаблону
    context_object_name = 'news'
    # extra_context = {'title':'Список новостей'}
    # # Лучше использовать для статичных данных.
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # В переменную 'context' записали все то,
        # что было там до этого (Все данные)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):  # Получаем отфильтрованный набор объектов
        return News.objects.\
            filter(is_published=True).select_related('category')

# def index(request):
#     #print(dir(request))
#     news = News.objects.all()
#     context = {
#         'news':news,
#         'title':'Список новостей',
#         }
        
#     return render(request,'news/index.html',context)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    # Когда список пуст, т.е записей нет, то смысла показывать его нет.
    # queryset = News.objects.select_related('category')
    #  Альтернатива методу get_queryset(self)
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # В переменную 'context' записали все то,
        # что было там до этого (Все данные)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        # в self можно получить параметры URL
        return News.objects.\
            filter(category_id=self.kwargs['category_id'],
                   is_published=True).select_related('category')

# def get_category(request,category_id):
#     news = News.objects.filter(category_id = category_id)
#     # category = Category.objects.get(pk = category_id)
#     category = get_object_or_404(Category,pk = category_id)
#     context = {
#         'news':news,
#         'category':category
#     }
#     return render(request,'news/category.html',context)


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = "news_item"

# def view_news(request,news_id):
#     # news_item = News.objects.get(pk = news_id)
#     news_item = get_object_or_404(News,pk = news_id)
#     return render(request,'news/view_news.html',{'news_item':news_item})


class CreateNews(LoginRequiredMixin, CreateView):
    # Нужно связать данный класс с формой
    form_class = NewsForm  # Указываем нужный нам класс формы
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home') #Если не написать,
    # то по умолчанию будет вызываться get_absolute_url той модели,
    # которая подвязана
    # login_url = '/admin/'
    raise_exception = True 


# Работа с Формами, несвязанными с моделями
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST) # Форма, связанная с данными.
# Все данные, введенные пользователем, не удалятся после submit.
#         if form.is_valid(): # Проверка: прошли данные валидацию,
# которые были настроены в модуле 'forms.py' для каждого поля
#             # print(form.cleaned_data)  # После того, как форма прошла
# Валидацию, то все данные, которые были введены,
# попадают в словарь 'cleaned_data'
#             #news = News.objects.create(**form.cleaned_data)
# # Две звездочки автоматически распакуют данный словарь и
# присвоит ключам автоматически соответствующие значения.
# Create также возвращает полученный объект
#             news = form.save()
#             return redirect(news) # Универсальный метод redirect.
# Можно указывать name из url куда
# мы хотим пойти или как видно сам экземпляр класса.
#     else:
#         form = NewsForm() # Форма, несвязанная с данными
#     return render(request,'news/add_news.html',{'form':form})
