# Generated by Django 2.1.3 on 2018-12-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssai', '0003_auto_20181120_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='exam_date_time',
            field=models.DateTimeField(blank=True, help_text='Exam Date and Time', null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='sit_location',
            field=models.CharField(default='', help_text='Exam Sit and Hall Location', max_length=200),
        ),
    ]
