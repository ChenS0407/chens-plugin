# Generated by Django 2.2.6 on 2021-08-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="finish_at",
            field=models.DateTimeField(null=True, verbose_name="finish time"),
        ),
    ]
