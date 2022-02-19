# Generated by Django 3.2.12 on 2022-02-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_galery_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='galery',
            name='Book',
            field=models.FileField(default=1, upload_to='books/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='galery',
            name='Photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
