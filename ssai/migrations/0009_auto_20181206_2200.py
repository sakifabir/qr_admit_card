# Generated by Django 2.1.3 on 2018-12-06 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssai', '0008_auto_20181206_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='qrcode_img',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='qr_code/'),
        ),
    ]
