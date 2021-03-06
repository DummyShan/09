# Generated by Django 4.0.4 on 2022-05-13 19:11

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_studentlist_contact_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='high_school',
            field=models.CharField(max_length=50, validators=[main.validators.validate_names], verbose_name='High School'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='name',
            field=models.CharField(max_length=50, validators=[main.validators.validate_names], verbose_name='Name:'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='steward_name',
            field=models.CharField(max_length=50, validators=[main.validators.validate_names], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_college',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[main.validators.validate_names], verbose_name='Previous College'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_course',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[main.validators.validate_names], verbose_name='Previous Program'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_name',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[main.validators.validate_names], verbose_name='Name'),
        ),
    ]
