# Generated by Django 2.2.1 on 2019-05-21 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='phone_number',
            new_name='contact',
        ),
    ]
