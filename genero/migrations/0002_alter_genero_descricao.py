# Generated by Django 3.2.4 on 2021-06-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
    ]
