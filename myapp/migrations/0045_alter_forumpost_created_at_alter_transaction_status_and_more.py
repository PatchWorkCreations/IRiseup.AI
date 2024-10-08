# Generated by Django 4.2.11 on 2024-09-15 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0044_lesson_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('success', 'Success'), ('pending', 'Pending'), ('error', 'Error')], db_index=True, default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userlessonprogress',
            name='completed',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
