# Generated by Django 4.1.3 on 2022-12-28 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_student_s_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="s_moblie",
            field=models.CharField(
                max_length=10,
                null=True,
                validators=[
                    django.core.validators.MaxLengthValidator(10),
                    django.core.validators.MinLengthValidator(10),
                ],
            ),
        ),
    ]
