from functools import reduce
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail, mail_admins
from .models import Categories, Item


def index(request):
    item = Item.objects.all()
    categories = Categories.objects.all()
    return render(request, 'index.html', {'data': item, 'category': categories})

def buy(request, id):
    item = Item.objects.get(id = id)
    img = f'/media/{item.file}'
    return render(request, 'buy.html', {'data': item, 'img': img})

def category(request, slug):
    categories = Categories.objects.all()
    item = Item.objects.all().filter(category=slug)
    return render(request, 'index.html', {'data': item, 'category': categories})

def basket(request):
    items = []
    for key, value in request.session.items():
        if 'basket' in key:
            items.append(Item.objects.get(id = value))
    return render(request, 'basket.html', {'data': items})

def basket_add(request, id):
    item = Item.objects.get(id = id)
    request.session[f'basket_{id}'] = item.id
    return redirect('/basket')

def basket_delete(request, id):
    del request.session[f'basket_{id}']
    return redirect('/basket')

def order(request):
    if request.method == 'POST':
        sum = request.POST['hidden_full_amount']
        return render(request, 'order.html', {'data': sum})

def order_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        tel = request.POST['tel']
        email = request.POST['email']
        data = f'{name} {surname} {tel} {email}'
        #send_mail('Заказ оформлен','Успешно оформлен заказ!','django',['tovstogan.vlad@gmail.com'],fail_silently=False,)
        #mail_admins('Новый заказ', data, fail_silently=False)
        return redirect('/')
    