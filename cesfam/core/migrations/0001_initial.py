# Generated by Django 4.2.1 on 2023-06-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_medicamento', models.CharField(max_length=25)),
                ('fecha_elab_medicamento', models.DateField(null=True)),
                ('fecha_venc_medicamento', models.DateField(null=True)),
                ('cantidad_medicamento', models.CharField(max_length=4)),
            ],
        ),
    ]
