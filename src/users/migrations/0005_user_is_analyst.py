# Generated by Django 3.2.12 on 2024-02-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210317_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_analyst',
            field=models.BooleanField(default=False),
        ),
    ]
