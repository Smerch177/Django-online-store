# Generated by Django 3.2.4 on 2021-06-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[], default='Прочее', max_length=300, verbose_name='Категория'),
        ),
    ]