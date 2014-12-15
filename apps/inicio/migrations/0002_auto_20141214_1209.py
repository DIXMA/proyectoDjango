# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busqueda',
            name='creado',
            field=models.DateTimeField(verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
