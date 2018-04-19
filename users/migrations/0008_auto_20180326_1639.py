# Generated by Django 2.0.3 on 2018-03-26 13:39

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_auto_20180326_1639'),
        ('users', '0007_auto_20180323_1652'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artiste',
        ),
        migrations.DeleteModel(
            name='Retailer',
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(blank=True, upload_to='documents/python/artbid/users/static/uploads/customuser/profile/'),
        ),
    ]