# Generated by Django 2.0.7 on 2018-08-09 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily_habits', '0004_auto_20180808_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
