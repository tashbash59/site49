# Generated by Django 3.2.12 on 2022-02-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]