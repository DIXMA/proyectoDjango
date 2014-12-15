# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20141214_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busqueda',
            name='creado',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
