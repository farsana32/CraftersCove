# Generated by Django 5.0 on 2024-01-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='soft_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
