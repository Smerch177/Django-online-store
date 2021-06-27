from my_site.settings import TEMPLATES
from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=300)

    def __repr__(self) -> str:
         return f'{self.id} _ {self.category}'

    def __str__(self) -> str:
        return self.category

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class Item(models.Model):
    title = models.TextField('Название предмета', null=False)
    price = models.IntegerField('Цена предмета', null=False)
    isActive = models.BooleanField('IsActive', default=True)
    text = models.TextField('Введите описание', null=False)
    category = models.CharField('Категория', max_length=300, choices = tuple((x.category, x.category) for x in Categories.objects.all()), default='Прочее')
    file = models.ImageField('Загрузить фото')

    def __repr__(self) -> str:
         return f'{self.title}'

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Discount(models.Model):
    title = models.TextField('Название предмета', null=False)
    price = models.IntegerField('Цена предмета', null=False)
    isActive = models.BooleanField('IsActive', default=True)
    text = models.TextField('Введите описание', null=False)
    category = models.CharField('Категория', max_length=300, choices = tuple((x.category, x.category) for x in Categories.objects.all()), default='Прочее')
    file = models.ImageField('Загрузить фото')

    def __repr__(self) -> str:
         return f'{self.title}'

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Скидки'
        verbose_name_plural = 'Скидки'

class Order(models.Model):
    name = models.TextField('Имя', null=False)
    surname = models.TextField('Фамилия', null=False)
    tel = models.TextField('Телефон', null=False)
    email = models.EmailField('email')
    title = models.TextField('Название предмета', null=False)
    price_amount = models.IntegerField('Цена предмета', null=False)
    amount = models.IntegerField('Количество', null=False)

    def __repr__(self) -> str:
         return f'{self.name} {self.surname} - {self.title}'

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Comments(models.Model):
    email = models.EmailField('email')
    title = models.TextField('Название предмета', null=False)
    comment = models.TextField('Комментарий', null=False)
    price = models.IntegerField('Цена', null=False)

    def __repr__(self) -> str:
         return f'{self.title}'

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Коментарии'
        verbose_name_plural = 'Коментарии'
