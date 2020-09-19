# Generated by Django 3.0 on 2020-09-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autoevaluaciones',
            fields=[
                ('clave', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='codigo')),
                ('fiebre', models.BooleanField()),
                ('tos', models.BooleanField()),
                ('diarrea', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')])),
                ('dolor_garganta', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')])),
                ('dificultad_respiratoria', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')])),
                ('dolor_muscular', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')])),
                ('cefalea', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')])),
                ('vomito', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')])),
                ('gusto_olfato', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')])),
                ('resultado', models.CharField(max_length=10)),
            ],
        ),
    ]
