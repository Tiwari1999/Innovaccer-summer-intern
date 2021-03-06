# Generated by Django 2.2.7 on 2019-11-20 20:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0003_auto_20191120_1910'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='VisitorEntry',
        ),
        migrations.AddField(
            model_name='user',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Host', 'Host'), ('Visitor', 'Visitor')], default='Host', max_length=30),
            preserve_default=False,
        ),
    ]
