## Copyright (c) 2011 by Jose Antonio Martin <jantonio.martin AT gmail DOT com>
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU Affero General Public License as published by the
## Free Software Foundation, either version 3 of the License, or (at your option
## any later version.
##
## This program is distributed in the hope that it will be useful, but WITHOUT
## ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License
## for more details.
##
## You should have received a copy of the GNU Affero General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/agpl.txt>.
##
## This license is also included in the file COPYING
##
## AUTHOR: Jose Antonio Martin <jantonio.martin AT gmail DOT com>

""" Definitions for common classes that are related to more than one app

"""

from django.db import models
from django.conf import settings

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

import logging
logger = logging.getLogger(__name__)

from machiavelli.signals import game_finished

class Server(models.Model):
    """ Defines core attributes for the whole site """
    ranking_last_update = models.DateTimeField()
    ranking_outdated = models.BooleanField(default=False)

    def __str__(self):
        return "Server %s" % self.pk

    def outdate_ranking(self):
        self.ranking_outdated = True
        self.save()

def outdate_ranking(sender, **kwargs):
    try:
        server = Server.objects.get()
    except MultipleObjectsReturned:
        logger.error("Multiple servers found")
    except ObjectDoesNotExist:
        logger.error("No configured server")
    else:
        server.outdate_ranking()

game_finished.connect(outdate_ranking)
