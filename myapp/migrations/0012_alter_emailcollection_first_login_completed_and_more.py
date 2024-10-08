# Generated by Django 4.2.11 on 2024-08-18 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0011_alter_quizresponse_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcollection',
            name='first_login_completed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='quizresponse',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
