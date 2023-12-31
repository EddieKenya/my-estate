# Generated by Django 4.2.2 on 2023-06-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_photo",
            field=models.ImageField(
                default="blank-prof.jpg",
                upload_to="profileimg",
                verbose_name="Profile Photo",
            ),
        ),
    ]
