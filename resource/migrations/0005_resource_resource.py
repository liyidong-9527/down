# Generated by Django 3.0.6 on 2020-06-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0004_auto_20200616_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='resource',
            field=models.FileField(blank=True, upload_to='resource/resource_upload/'),
        ),
    ]