# Generated by Django 2.0.7 on 2018-08-15 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_habits', '0008_delete_habit'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='eatStreak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='exerciseStreak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='meditateStreak',
            field=models.IntegerField(default=0),
        ),
    ]
