# Generated by Django 4.2.11 on 2024-08-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_usercourseaccess_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourseaccess',
            name='renewal_task_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
