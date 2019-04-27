# -*- coding: utf-8 -*-
'''Zerto Datastore object'''

from zertoobject import ZertoObject


class Datastore(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['DatastoreName']
        self.identifier = kwargs['DatastoreIdentifier']

    def __str__(self):
        return 'name={0}, identifier={1}'.format(
            self.name, self.identifier)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
