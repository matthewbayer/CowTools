# Generated by Django 3.2.5 on 2022-01-29 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220128_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pressreleasesubmission',
            old_name='request_id',
            new_name='submission_id',
        ),
        migrations.AddField(
            model_name='pressreleasesubmission',
            name='error_msg',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pressreleasesubmission',
            name='submission_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETE', 'Complete'), ('ERROR', 'Error')], default='PENDING', max_length=255),
        ),
    ]
