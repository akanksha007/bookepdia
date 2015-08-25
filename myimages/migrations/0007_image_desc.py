# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myimages', '0006_delete_formimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='desc',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
