# Generated by Django 2.0.7 on 2018-08-18 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily_habits', '0010_auto_20180816_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='eatHealthyCompleted',
            new_name='habitOneCompleted',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='exerciseCompleted',
            new_name='habitThreeCompleted',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='meditateCompleted',
            new_name='habitTwoCompleted',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='eatHealthy',
            new_name='habitOne',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='exercise',
            new_name='habitThree',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='meditate',
            new_name='habitTwo',
        ),
    ]