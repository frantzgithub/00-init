# Generated by Django 5.0.2 on 2024-03-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_email_alter_account_passport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_married',
            field=models.BooleanField(default=False),
        ),
    ]
