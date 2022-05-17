# Generated by Django 4.0.4 on 2022-05-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_studentlist_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='birthdate',
            field=models.DateField(verbose_name='Birthdate (YYYY-MM-DD)'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='college',
            field=models.CharField(choices=[('College of Agriculture', 'College of Agriculture'), ('College of Arts and Sciences', 'College of Arts and Sciences'), ('College of Computer Studies', 'College of Computer Studies'), ('College of Engineering', 'College of Engineering'), ('College of Nursing', 'College of Nursing'), ('School of Business and Management', 'School of Business and Management'), ('College of Education', 'College of Education')], max_length=50),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='if_transferee',
            field=models.BooleanField(default=False, verbose_name='If Transferee'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name:'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='year',
            field=models.CharField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year')], max_length=8, verbose_name='Year Level'),
        ),
    ]
