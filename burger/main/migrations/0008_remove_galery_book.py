# Generated by Django 3.2.12 on 2022-02-17 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220217_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galery',
            name='Book',
        ),
    ]
