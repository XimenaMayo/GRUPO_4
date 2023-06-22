# Generated by Django 4.2.1 on 2023-06-21 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=100, verbose_name='Nombre y apellido')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('teléfono', models.CharField(max_length=256, verbose_name='Teléfono de contacto')),
                ('informacion_detallada_de_alumno', models.CharField(max_length=500, null=True, verbose_name='Información detallada del alumno')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=100, verbose_name='Nombre y apellido')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('teléfono', models.CharField(max_length=256, verbose_name='Teléfono de contacto')),
                ('profesión', models.BooleanField(verbose_name='Titulo profesional')),
                ('entrevistas', models.BooleanField(verbose_name='Entrevistas aprobadas')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfoAlumno',
            fields=[
                ('dni', models.DateField(max_length=10, verbose_name='DNI')),
                ('dirección', models.CharField(max_length=200, verbose_name='Dirección')),
                ('fecha_ingreso', models.DateField(default='1900-01-01', verbose_name='Fecha de ingreso')),
                ('alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Articulos.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('número_comisión', models.IntegerField(verbose_name='Número de comisión')),
                ('alumnos', models.ManyToManyField(to='Articulos.alumno')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articulos.profesor')),
            ],
        ),
    ]