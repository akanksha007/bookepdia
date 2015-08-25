# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myimages', '0005_formimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FormImage',
        ),
    ]
