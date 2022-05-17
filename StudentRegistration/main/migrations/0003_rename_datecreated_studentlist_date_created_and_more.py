# Generated by Django 4.0.4 on 2022-05-01 11:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_studentlist_id_alter_studentlist_exam_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentlist',
            old_name='dateCreated',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='contact_number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(99999999999)]),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='gpa',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='year',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(1)]),
        ),
    ]