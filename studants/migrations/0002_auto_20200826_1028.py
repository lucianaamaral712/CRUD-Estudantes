# Generated by Django 3.0.7 on 2020-08-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studant',
            name='course',
            field=models.CharField(choices=[('Ciência da Computação', 'Ciência da Computação'), ('Física', 'Física'), ('Enfermagem', 'Enfermagem'), ('Engenharia Civil', 'Engenharia Civil'), ('Arquitetura', 'Arquitetura'), ('Química', 'Química')], max_length=50),
        ),
    ]
