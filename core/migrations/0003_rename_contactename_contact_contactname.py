# Generated by Django 4.1.1 on 2022-10-27 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_reason_contact_contactphone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contactename',
            new_name='contactname',
        ),
    ]