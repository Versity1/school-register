# Generated by Django 5.2.2 on 2025-06-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0002_alter_biodata_height_alter_biodata_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='student_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
