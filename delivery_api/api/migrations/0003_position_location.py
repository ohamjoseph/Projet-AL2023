# Generated by Django 4.1.7 on 2023-04-02 14:13

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_produit_coli'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='location',
            field=location_field.models.plain.PlainLocationField(default=0, max_length=63),
            preserve_default=False,
        ),
    ]
