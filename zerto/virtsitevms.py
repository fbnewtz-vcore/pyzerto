# -*- coding: utf-8 -*-
'''Zerto protected VM object'''

from zertoobject import ZertoObject


class VirtSiteVMs(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['VmName']
        self.identifier = kwargs['VmIdentifier']

    def __str__(self):
        return 'name={0}, identifier={1}'.format(
            self.name, self.identifier)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
