# Generated by Django 4.2.11 on 2024-08-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_usercourseaccess_renewal_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourseaccess',
            name='selected_plan',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
