# Generated by Django 4.2.4 on 2023-08-18 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_user_review_user_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_review',
            name='user_rating',
            field=models.CharField(choices=[('1', '1 - Poor'), ('2', '2 - Fair'), ('3', '3 - Good'), ('4', '4 - Very Good'), ('5', '5 - Excellent')], default='1'),
        ),
    ]