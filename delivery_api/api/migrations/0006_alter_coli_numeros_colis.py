# Generated by Django 4.1.7 on 2023-04-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_position_coli'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coli',
            name='numeros_colis',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
