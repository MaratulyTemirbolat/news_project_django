from django.urls import path
# from django.views.decorators.cache import cache_page

from .views import (
    user_login,
    register,
    HomeNews,
    NewsByCategory,
    ViewNews,
    CreateNews,
    test,
    user_logout,
    contact_email,
)

urlpatterns = [
    path('contact_form/', contact_email, name='contact'),
    path('login/', user_login, name="login"),
    path('register/', register, name="register"),
    path('logout/', user_logout, name="logout"),
    path('test/', test, name='test'),
    # path('',index,name = 'home'),
    # path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/',get_category, name = 'category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Какой-то тайтл'}), name = 'category'),
    # path('news/<int:news_id>/',view_news,name = "view_news"),
    path('news/<int:pk>/', ViewNews.as_view(), name="view_news"),
    # path('news/add-news/',add_news,name = 'add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news')
]
