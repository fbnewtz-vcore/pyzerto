# -*- coding: utf-8 -*-
'''Zerto Datastore object'''

from zertoobject import ZertoObject


class Datastore(ZertoObject):

    def __init__(self, *args):
        self.values = args
        self.name = args['DatastoreName']
        self.identifier = args['DatastoreIdentifier']
#        self.type = kwargs.get('Type')
#        self.capacityinbytes = kwargs.get('CapactiyInBytes')
#        self.freeinbytes = kwargs.get('FreeInBytes')
#        self.provisionedinbytes = kwargs.get('ProvisionedInBytes')
#        self.usedinbytes = kwargs.get('UsedInBytes')

    def __str__(self):
        return 'name={0}, identifier={1}'.format(
            self.name, self.identifier)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
