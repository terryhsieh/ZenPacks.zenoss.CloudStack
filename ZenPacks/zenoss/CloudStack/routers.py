###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2011, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul


class CloudStackRouter(DirectRouter):
    def _getFacade(self):
        return Zuul.getFacade('cloudstack', self.context)

    def add_cloudstack(self, url, api_key, secret_key):
        facade = self._getFacade()
        success, message = facade.add_cloudstack(
            url, api_key, secret_key)

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)
