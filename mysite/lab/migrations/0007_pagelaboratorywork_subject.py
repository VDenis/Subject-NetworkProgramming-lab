# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_auto_20141017_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelaboratorywork',
            name='subject',
            field=models.ForeignKey(default=0, to='lab.Subject'),
            preserve_default=False,
        ),
    ]
