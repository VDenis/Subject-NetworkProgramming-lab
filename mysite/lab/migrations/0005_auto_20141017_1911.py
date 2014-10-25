# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20141017_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelaboratorywork',
            name='student',
            field=models.ForeignKey(default=0, to='lab.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagelaboratorywork',
            name='subject',
            field=models.ManyToManyField(to='lab.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='professor',
            field=models.ForeignKey(default=0, to='lab.Professor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=75),
        ),
    ]
