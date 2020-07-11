# Generated by Django 3.0.6 on 2020-06-14 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='账户', max_length=200)),
                ('password', models.CharField(help_text='密码', max_length=50)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(help_text='昵称', max_length=20)),
                ('realname', models.CharField(help_text='真实姓名', max_length=20)),
                ('user_email', models.EmailField(help_text='邮箱', max_length=254)),
                ('user_phone', models.CharField(help_text='联系方式', max_length=20)),
                ('sex', models.CharField(help_text='性别', max_length=1)),
                ('photo', models.FileField(upload_to='')),
                ('reg_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
