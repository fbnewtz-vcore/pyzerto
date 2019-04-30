# -*- coding: utf-8 -*-
'''Zerto VPG object'''

from zertoobject import ZertoObject
from constants import vpg_status, vpg_sub_status


class vpgSettings(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['VpgName']
        self.identifier = kwargs['VpgIdentifier']
        self.priority = kwargs.get('Priority')
        self.source_site = kwargs.get('SourceSite')
        self.target_site = kwargs.get('TargetSite')

    def __str__(self):
        return 'name={0}, identifier={1}'.format(
            self.name, self.identifier)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
