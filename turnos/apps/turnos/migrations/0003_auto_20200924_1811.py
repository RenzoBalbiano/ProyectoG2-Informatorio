# Generated by Django 3.0 on 2020-09-24 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0008_auto_20200923_2106'),
        ('turnos', '0002_auto_20200923_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='id_local',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_idLocal', to='empresa.Empresa'),
        ),
    ]
