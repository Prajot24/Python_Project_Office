# Generated by Django 3.2.12 on 2024-02-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_analysis'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscribe_analysts',
            field=models.ManyToManyField(related_name='_users_user_subscribe_analysts_+', to='users.Analysis', verbose_name='Analyst'),
        ),
    ]
