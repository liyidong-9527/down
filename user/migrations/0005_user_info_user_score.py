# Generated by Django 3.0.6 on 2020-06-16 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200615_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='user_score',
            field=models.CharField(default=20, help_text='积分', max_length=100),
        ),
    ]