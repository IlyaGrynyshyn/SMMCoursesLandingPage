# Generated by Django 4.1.7 on 2023-03-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_recording', '0004_alter_pre_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pre_registration',
            name='date',
            field=models.DateTimeField(),
        ),
    ]