# Generated by Django 4.0.3 on 2022-03-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_user_book1_user_book2_user_book3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='book1',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='book2',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='book3',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]