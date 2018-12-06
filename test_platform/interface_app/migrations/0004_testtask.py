# Generated by Django 2.1.1 on 2018-11-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0003_auto_20181119_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('describe', models.TextField(default='', verbose_name='描述')),
                ('cases', models.TextField(default='', verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]