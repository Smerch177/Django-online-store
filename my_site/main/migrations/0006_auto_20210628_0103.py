# Generated by Django 3.2.4 on 2021-06-27 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('title', models.TextField(verbose_name='Название предмета')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': 'Скидки', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
