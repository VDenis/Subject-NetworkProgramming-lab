# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_subject_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(default=01, to='lab.Group'),
            preserve_default=False,
        ),
    ]
