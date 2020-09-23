# Generated by Django 3.0 on 2020-09-22 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='DNI',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='invitado1',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_invitado1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='invitado2',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_invitado2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='invitado3',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_invitado3', to=settings.AUTH_USER_MODEL),
        ),
    ]
