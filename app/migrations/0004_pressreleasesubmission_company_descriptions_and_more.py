# Generated by Django 4.0 on 2022-01-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customuser_email_confirmed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressreleasesubmission',
            name='company_descriptions',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pressreleasesubmission',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pressreleasesubmission',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pressreleasesubmission',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='pressreleasesubmission',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pressreleasesubmission',
            name='generated_text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pressreleasesubmission',
            name='rating',
            field=models.BooleanField(null=True, verbose_name='whether or not the user gave the generation a thumbs up'),
        ),
        migrations.AlterField(
            model_name='pressreleasesubmission',
            name='submission_date',
            field=models.DateTimeField(null=True),
        ),
    ]