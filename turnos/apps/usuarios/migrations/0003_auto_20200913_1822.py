# Generated by Django 3.0 on 2020-09-13 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_es_duenio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cumpleanio',
            field=models.DateField(null=True),
        ),
    ]