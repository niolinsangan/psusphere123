# Generated by Django 5.0 on 2024-11-06 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0003_alter_college_college_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='College',
            new_name='college',
        ),
        migrations.AlterField(
            model_name='college',
            name='college_name',
            field=models.CharField(max_length=150),
        ),
    ]
