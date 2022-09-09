# Generated by Django 3.2 on 2021-05-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя бота')),
                ('token', models.CharField(max_length=50, verbose_name='Токен бота')),
                ('call', models.CharField(max_length=15, verbose_name='Обращение бота')),
                ('time', models.PositiveIntegerField(verbose_name='Задержка перед отправкой сообщения')),
                ('voice', models.BooleanField(verbose_name='Ответ голосовыми сообщениями')),
                ('status', models.TextField(verbose_name='Статус')),
            ],
        ),
    ]