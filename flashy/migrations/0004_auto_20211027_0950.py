# Generated by Django 3.2.8 on 2021-10-27 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashy', '0003_auto_20211027_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='user',
        ),
    ]
