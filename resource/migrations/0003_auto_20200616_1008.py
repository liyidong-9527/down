# Generated by Django 3.0.6 on 2020-06-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0002_auto_20200616_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='content_type',
            field=models.CharField(blank=True, help_text='文件类型', max_length=20),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_key',
            field=models.CharField(help_text='关键字', max_length=50),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_type',
            field=models.CharField(help_text='资源类型', max_length=10),
        ),
    ]