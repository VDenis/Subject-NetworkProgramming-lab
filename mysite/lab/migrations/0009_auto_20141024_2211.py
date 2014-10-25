# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_auto_20141018_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madelaboratorywork',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='madelaboratorywork',
            name='upload_file',
            field=models.FileField(upload_to=b'documents', verbose_name=b'File', blank=True),
        ),
        migrations.AlterField(
            model_name='pagelaboratorywork',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pagelaboratorywork',
            name='document',
            field=models.FileField(upload_to=b'documents', verbose_name=b'File', blank=True),
        ),
    ]
