# Generated by Django 3.0 on 2020-09-22 20:16

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
            name='Razon_Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('CUIT', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='CUIT')),
                ('Nombre', models.CharField(max_length=50)),
                ('Superficie', models.PositiveIntegerField()),
                ('Cant_empleados', models.PositiveIntegerField()),
                ('DNI', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_usuario', to=settings.AUTH_USER_MODEL)),
                ('Razon_Social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='razon_social', to='empresa.Razon_Social')),
                ('Rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rubro_empresa', to='empresa.Rubro')),
            ],
        ),
    ]