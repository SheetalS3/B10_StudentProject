# Generated by Django 4.0 on 2023-11-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
