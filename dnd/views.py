
# Create your views here.

from django.shortcuts import render  
from .models import New

# news = [
#     {
#         'title': 'Первая запись',  
#         'text': 'Много-много текста',  
#         'date': '10 Мая 2020',  
#         'author': 'Валерий'  
#     },  
#     {  
#         'title': 'Вторая запись',  
#         'text': 'Снова много-много текста',  
#         'date': '19 Мая 2020',  
#         'author': 'Егор'  
#     }  
# ]  

# def home(request):  
#     data = {  
#         'news': news,  
#         'title': 'Главная страница'  
#     }  
#     return render(request, 'dnd/home.html', data)  


# def contacts(request):  
# 	data = {'title': 'Контакты'}  
# 	return render(request, 'dnd/contacts.html', data)


def home(request):
    data = {
        'news': New.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'dnd/home.html', data)


def contacts(request):
    return render(request, 'dnd/contacts.html', {'title': 'Контакты'})
