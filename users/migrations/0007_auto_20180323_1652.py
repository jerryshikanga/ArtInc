# Generated by Django 2.0.3 on 2018-03-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(blank=True, upload_to='./users/images/profile/'),
        ),
    ]
