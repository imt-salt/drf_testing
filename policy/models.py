from django.db import models


class Policy(models.Model):

    policy_number = models.CharField(max_length=10)


class Coverage(models.Model):

    policy = models.ForeignKey('Policy', related_name='coverages')
    liability = models.BooleanField(default=False)
    coverage_type = models.CharField(max_length=140)
