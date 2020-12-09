# Generated by Django 2.1.3 on 2018-12-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssai', '0004_auto_20181206_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='admit_pic',
            field=models.ImageField(default='pic_folder/default.png', help_text='Students Picture on Admit Card', upload_to='pic_folder/'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='roll_no',
            field=models.CharField(help_text="Student's Roll Number", max_length=50, unique=True),
        ),
    ]
