#! /usr/bin/env python
# coding: utf-8

from django.db import models

# Create your models here.

class doamin(models.Model):
    """
    域名信息
    """
    name=models.CharField(max_length=20, verbose_name='domain名称')
    domain_id=models.CharField(max_length=20, verbose_name='domain_id')

    def __unicode__(self):
        return self.name



class dnspod_info(models.Model):
    """
    dnspod接口相关信息
    """
    name=models.CharField(max_length=20, verbose_name='姓名')
    desc=models.CharField(max_length=100, blank=True,null=True,verbose_name='描述')
    dnspod_id=models.IntegerField(verbose_name=u'dnspod ID')
    dnspod_token=models.IntegerField(verbose_name=u'dnspod TOKEN')

    class Meta():
        unique_together = ("dnspod_id", "dnspod_token")

    def __unicode__(self):
        return name

    def get_login_token(self):
        return '$s,%s' %(dnspod_id,dnspod_token)






