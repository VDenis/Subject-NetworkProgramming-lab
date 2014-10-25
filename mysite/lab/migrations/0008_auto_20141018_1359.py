# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lab', '0007_pagelaboratorywork_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='surname',
        ),
        migrations.AddField(
            model_name='professor',
            name='user',
            field=models.OneToOneField(default=3, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=3, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
