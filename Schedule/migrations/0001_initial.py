# Generated by Django 3.1.5 on 2021-02-06 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(help_text='Время в формате h:m-h:m', max_length=100, verbose_name='время')),
                ('date', models.DateField(help_text='Дата в формате YYYY-MM-DD', verbose_name='дата')),
                ('affair', models.CharField(help_text='Дела должны быть в виде обычного текста', max_length=200, verbose_name='дело')),
                ('note', models.CharField(help_text='Заметки должны быть в виде обычного текста', max_length=200, verbose_name='заметка')),
                ('homework', models.CharField(default=None, help_text='Домашнее задание должны быть в виде обычного текста', max_length=200, verbose_name='домашнее задание')),
                ('is_ready', models.BooleanField(default=False, help_text='Готово? принимает только значение True или False', verbose_name='готово?')),
                ('user_id', models.ForeignKey(help_text='Id пользователя должен быть в виде одного числа', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id пользователя')),
            ],
            options={
                'verbose_name': 'расписание',
                'verbose_name_plural': 'расписании',
                'ordering': ['date'],
                'managed': True,
            },
        ),
    ]
