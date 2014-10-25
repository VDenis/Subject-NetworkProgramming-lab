# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_auto_20141017_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('comment', models.CharField(max_length=1000)),
                ('made_laboratory_work', models.ForeignKey(to='lab.MadeLaboratoryWork')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pagelaboratorywork',
            name='student',
        ),
        migrations.RemoveField(
            model_name='pagelaboratorywork',
            name='subject',
        ),
        migrations.AddField(
            model_name='madelaboratorywork',
            name='page_laboratory_work',
            field=models.ForeignKey(default=0, to='lab.PageLaboratoryWork'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='madelaboratorywork',
            name='student',
            field=models.ForeignKey(default=0, to='lab.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='department',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
    ]
