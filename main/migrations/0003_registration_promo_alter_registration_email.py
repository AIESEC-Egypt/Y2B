# Generated by Django 5.0.6 on 2025-03-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_registration_aiesecer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='promo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
