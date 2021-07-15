# Generated by Django 3.2.4 on 2021-07-15 15:13

import django.core.validators
from django.db import migrations, models
import usr_val.models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_val', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cv',
            field=models.FileField(null=True, upload_to=usr_val.models.cv_upload_location, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('BT', 'BIOTECHNOLOGY'), ('CE', 'CIVIL ENGINEERING'), ('CH', 'CHEMICAL ENGINEERING'), ('CS', 'COMPUTER SCIENCE & ENGINEERING'), ('CY', 'CHEMISTRY'), ('EC', 'ELECTRONICS AND COMMUNICATION ENGINEERING'), ('EE', 'ELECTRICAL ENGINEERING'), ('ES', 'EARTH & ENVIRONMENTAL STUDIES'), ('HS', 'HUMANITIES AND SOCIAL SCIENCES'), ('MA', 'MATHEMATICS'), ('ME', 'MECHANICAL ENGINEERING'), ('MM', 'META'), ('MS', 'MANAGEMENT'), ('PH', 'PHY')], max_length=3),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='branch',
            field=models.CharField(choices=[('BT', 'BIOTECHNOLOGY'), ('CE', 'CIVIL ENGINEERING'), ('CH', 'CHEMICAL ENGINEERING'), ('CS', 'COMPUTER SCIENCE & ENGINEERING'), ('CY', 'CHEMISTRY'), ('EC', 'ELECTRONICS AND COMMUNICATION ENGINEERING'), ('EE', 'ELECTRICAL ENGINEERING'), ('ES', 'EARTH & ENVIRONMENTAL STUDIES'), ('HS', 'HUMANITIES AND SOCIAL SCIENCES'), ('MA', 'MATHEMATICS'), ('ME', 'MECHANICAL ENGINEERING'), ('MM', 'META'), ('MS', 'MANAGEMENT'), ('PH', 'PHY')], max_length=3),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='contact',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
