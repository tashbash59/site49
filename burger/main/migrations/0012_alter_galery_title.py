# Generated by Django 3.2.12 on 2022-02-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_galery_advert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galery',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]