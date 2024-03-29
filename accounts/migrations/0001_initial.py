# Generated by Django 5.0.2 on 2024-03-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('passport', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField(null=True)),
                ('is_married', models.BooleanField(default=True)),
            ],
        ),
    ]
