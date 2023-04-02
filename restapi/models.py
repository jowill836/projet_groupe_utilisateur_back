from django.db import models

class Configuration(models.Model):
    nbgrp = models.IntegerField()
    nbusr = models.IntegerField()
    minmax = models.IntegerField()

class Usrs(models.Model):
    usr_id = models.AutoField(primary_key=True)
    nameusr = models.CharField(max_length=255)
    grp_id = models.ForeignKey('Grp', models.SET_NULL,
    blank=True,
    null=True,)

class Grp(models.Model):
    grp_id = models.AutoField(primary_key=True)
    namegrp = models.CharField(max_length=255)
    islast = models.IntegerField(default=None, blank=True, null=True)


