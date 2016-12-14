#! /usr/bin/env python
# coding:utf-8

# Create your models here.
from django.db import models
from domain_op import models


class User(models.Model):
    state_options = ((1, '正常'), (0, '禁用'))

    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='角色')
    sub_doamin = models.ManyToManyField(sub_domain, verbose_name='子域名授权')
    # person_id = models.CharField(max_length=40, unique=True, verbose_name='员工ID(OA)')
    name = models.CharField(max_length=20, verbose_name='姓名')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    state = models.SmallIntegerField(choices=state_options, default=state_options[0][0], verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ('id',)

    def __unicode__(self):
        if self.email:
            email = self.email.split('@')
            return '%s - %s' % (email[0], self.name)
        else:
            return self.name

    def get_site_list(self):
        return [sub_doamin.id for sub_doamin in self.sub_doamin.all()]

    def get_site_list_display(self):
        return ', '.join([str(sub_doamin) for sub_doamin in self.sub_doamin.all()])


class Role(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='名称')
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='描述')
    permission = models.TextField(blank=True, verbose_name='权限')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ('id',)

    def __unicode__(self):
        return self.name

    def get_permission_list(self):
        if self.permission is not None and len(self.permission) > 0:
            permission_list = self.permission.split(',')  # 把数据库中的str转化为list，方便使用
        else:
            permission_list = list()
        return permission_list


permission_list = (
    {'name': u'创建域名',
     'urls': ({'url': ('monitor_data.index',), 'name': u'创建'},)},
    {'name': u'子域名管理',
     'childs': ({'name': u'子域名管理',
                 'urls': ({'url': ('product.index',), 'name': u'浏览'},
                          {'url': ('product.add',), 'name': u'添加'},
                          {'url': ('product.edit',), 'name': u'编辑'},
                          {'url': ('product.delete',), 'name': u'删除'},)},
    {'name': u'日志管理',
     'childs': ({'name': u'操作日志',
                 'urls': ({'url': ('operator_log.index', 'operator_log.detail',), 'name': u'浏览'},)},)},
)