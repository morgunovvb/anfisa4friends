# ice_cream/views.py
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader
# Импортируем рендеринг
from django.shortcuts import render


# Главная страница
def index(request):
    template = 'ice_cream/index.html'
    return render(request, template)

# Страница со списком мороженого
def ice_cream_list(request):
    template = 'ice_cream/ice_cream_list.html'
    return render(request, template)

# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def ice_cream_detail(request, pk):
    template = 'ice_cream/ice_cream_detail.html'
    return render(request, template)