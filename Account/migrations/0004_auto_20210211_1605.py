# Generated by Django 3.1.6 on 2021-02-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20210211_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educational_organization',
            name='name',
            field=models.CharField(max_length=150, verbose_name='образовательная организация'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='name',
            field=models.CharField(max_length=150, verbose_name='населённый пункт'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=150, verbose_name='городской округ / Муниципальный район'),
        ),
        migrations.AlterField(
            model_name='type_of_oo',
            name='name',
            field=models.CharField(max_length=150, verbose_name='тип ОО'),
        ),
    ]
