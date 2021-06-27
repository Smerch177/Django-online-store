from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=300)

    def __repr__(self) -> str:
         return f'{self.id} _ {self.category}'

class Item(models.Model):
    title = models.TextField('Название предмета', null=False)
    price = models.IntegerField('Цена предмета', null=False)
    isActive = models.BooleanField('IsActive', default=True)
    text = models.TextField('Введите описание', null=False)
    category = models.CharField('Категория', max_length=300, choices = tuple((x.category, x.category) for x in Categories.objects.all()), default='Прочее')
    file = models.ImageField('Загрузить фото')

    def __repr__(self) -> str:
         return f'{self.title}'

class Discount(models.Model):
    title = models.TextField('Название предмета', null=False)
    price = models.IntegerField('Цена предмета', null=False)
    isActive = models.BooleanField('IsActive', default=True)
    text = models.TextField('Введите описание', null=False)
    category = models.CharField('Категория', max_length=300, choices = tuple((x.category, x.category) for x in Categories.objects.all()), default='Прочее')
    file = models.ImageField('Загрузить фото')

    def __repr__(self) -> str:
         return f'{self.title}'
