# Generated by Django 4.0.4 on 2022-05-01 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_studentlist_country_previousuniversity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='previousuniversity',
            name='student',
        ),
        migrations.DeleteModel(
            name='ParentGuardian',
        ),
        migrations.DeleteModel(
            name='PreviousUniversity',
        ),
    ]
