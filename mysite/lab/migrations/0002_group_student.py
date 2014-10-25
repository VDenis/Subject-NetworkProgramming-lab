# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='student',
            field=models.ForeignKey(default=0, to='lab.Student'),
            preserve_default=False,
        ),
    ]
