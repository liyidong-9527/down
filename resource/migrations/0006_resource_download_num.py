# Generated by Django 3.0.6 on 2020-06-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0005_resource_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='download_num',
            field=models.CharField(default=0, help_text='下载次数', max_length=20),
        ),
    ]
