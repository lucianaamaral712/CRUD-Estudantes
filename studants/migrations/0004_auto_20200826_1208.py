# Generated by Django 3.0.7 on 2020-08-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studants', '0003_auto_20200826_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studant',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
