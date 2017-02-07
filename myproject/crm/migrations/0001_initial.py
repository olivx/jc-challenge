# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import myproject.crm.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'modificado em')),
                ('id', models.UUIDField(primary_key=True, default=myproject.crm.models._createHash, serialize=False, editable=False, unique=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'nome')),
                ('user', models.ForeignKey(related_name='company_user', verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
            },
        ),
    ]
