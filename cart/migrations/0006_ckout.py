# Generated by Django 4.1.1 on 2022-10-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_checkout_caddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='ckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfname', models.CharField(max_length=50)),
                ('caddress', models.CharField(max_length=50)),
            ],
        ),
    ]