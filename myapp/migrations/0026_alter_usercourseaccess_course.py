# Generated by Django 4.2.11 on 2024-08-27 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_usercourseaccess_renewal_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourseaccess',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course'),
        ),
    ]
