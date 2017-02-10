# -*- coding: utf-8 -*-
import uuid
from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class UUIDModel(models.Model):
    # Gera um uuid de 32 caracteres

    pk_uuid = models.UUIDField(editable=False, unique=True, null=True, db_index=True, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        'modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(u'endereço', max_length=100, blank=True)
    complement = models.CharField('complemento', max_length=100, blank=True)
    district = models.CharField('bairro', max_length=100, blank=True)
    city = models.CharField('cidade', max_length=100, blank=True)
    uf = models.CharField('UF', max_length=2,
                          choices=STATE_CHOICES, blank=True)
    cep = models.CharField('CEP', max_length=9, blank=True)

    class Meta:
        abstract = True
