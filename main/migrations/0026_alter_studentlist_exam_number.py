# Generated by Django 4.0.4 on 2022-05-14 02:14

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_studentlist_steward_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='exam_number',
            field=models.CharField(max_length=5, primary_key=True, serialize=False, validators=[main.validators.validate_exam_number], verbose_name='Exam Number'),
        ),
    ]
