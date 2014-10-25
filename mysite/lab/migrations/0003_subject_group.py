# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_group_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='group',
            field=models.ManyToManyField(to='lab.Group'),
            preserve_default=True,
        ),
    ]
