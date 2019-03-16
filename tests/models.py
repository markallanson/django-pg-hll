from django.db import models

from django_pg_hll import HllField


class FKModel(models.Model):
    pass


class TestModel(models.Model):
    hll_field = HllField()
    fk = models.ForeignKey(FKModel, null=True, blank=True, on_delete=models.CASCADE)

