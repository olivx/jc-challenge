# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='id',
            new_name='pk_uuid',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='id',
            new_name='pk_uuid',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='id',
            new_name='pk_uuid',
        ),
    ]
