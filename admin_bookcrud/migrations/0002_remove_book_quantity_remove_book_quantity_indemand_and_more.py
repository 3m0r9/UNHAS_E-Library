# Generated by Django 4.0 on 2022-01-23 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_bookcrud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='book',
            name='quantity_indemand',
        ),
        migrations.RemoveField(
            model_name='book',
            name='quantity_inlibrary',
        ),
        migrations.RemoveField(
            model_name='book',
            name='quantity_outlibrary',
        ),
    ]