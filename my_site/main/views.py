from functools import reduce
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail, mail_admins
from .models import Categories, Comments, Discount, Item, Order
from json import loads


def index(request):
    item = Item.objects.all()
    categories = Categories.objects.all()
    discount = Discount.objects.all()
    return render(request, 'index.html', {'data': item, 'category': categories, 'Discount': discount})

def buy(request, id):
    item = Item.objects.get(id = id)
    img = f'/media/{item.file}'
    return render(request, 'buy.html', {'data': item, 'img': img})

def discount(request, id):
    discount = Discount.objects.get(id = id)
    img = f'/media/{discount.file}'
    return render(request, 'discount.html', {'data': discount, 'img': img})

def category(request, slug):
    categories = Categories.objects.all()
    item = Item.objects.all().filter(category=slug)
    return render(request, 'index.html', {'data': item, 'category': categories})

def basket(request):
    items = []
    items_disk = []
    for key, value in request.session.items():
        if '_dis' in key:
            items_disk.append(Discount.objects.get(id = value))
        if 'basket' in key:
            items.append(Item.objects.get(id = value))
    return render(request, 'basket.html', {'data': items, 'discount': items_disk})

def basket_add(request, id):
    item = Item.objects.get(id = id)
    request.session[f'basket_{id}'] = item.id
    return redirect('/basket')

def basket_add_disk(request, id):
    discount = Discount.objects.get(id = id)
    request.session[f'{id}_dis'] = discount.id
    return redirect('/basket')

def basket_delete_disk(request, id):
    del request.session[f'{id}_dis']
    return redirect('/basket')

def basket_delete(request, id):
    del request.session[f'basket_{id}']
    return redirect('/basket')

def order(request):
    if request.method == 'POST':
        sum = request.POST['hidden_full_amount']
        json = request.POST['hidden_all_info_json']
        return render(request, 'order.html', {'data': sum, 'data_json': json})

def order_create(request):
    if request.method == 'POST':
        json = loads(request.POST['hidden_all_info_json'])
        for x in json:
            order = Order()
            order.name = request.POST['name']
            order.surname = request.POST['surname']
            order.tel = request.POST['tel']
            order.email = request.POST['email']
            order.title = x
            order.price_amount = int(json[f'{x}'][1])
            order.amount = int(json[f'{x}'][0])
            order.save()
            comments = Comments()
            comments.email = request.POST['email']
            comments.title = x
            comments.price = int(json[f'{x}'][1])
            comments.save()
        #send_mail('Заказ оформлен','Успешно оформлен заказ!','django',[email],fail_silently=False,)
        #mail_admins('Новый заказ', data, fail_silently=False)
        return redirect('/')

def comments(request):
    comments = Comments.objects.all()
    return render(request, 'comments.html', {'data': comments})

def comments_add(request):
    if request.method == 'POST':
        email = request.POST['email']
        comments = Comments.objects.all().filter(email = email)
        for x in comments:
            if x.comment == '':
                x.comment = request.POST['comment']
                x.save()
            else:
                pass
    return redirect('/comments')
        
    