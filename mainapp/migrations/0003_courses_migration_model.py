# Generated by Django 3.2.13 on 2022-05-29 22:38
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Courses",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256, verbose_name="Name")),
                ("description", models.TextField(blank=True, null=True, verbose_name="Description")),
                ("description_as_markdown", models.BooleanField(default=False, verbose_name="As markdown")),
                ("cost", models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name="Cost")),
                ("cover", models.CharField(default="no_image.svg", max_length=25, verbose_name="Cover")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Edited")),
                ("deleted", models.BooleanField(default=False)),
            ],
        )
    ]
