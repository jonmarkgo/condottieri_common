from datetime import datetime
import logging
from unittest.mock import patch

from django.test import TestCase

from condottieri_common.models import outdate_ranking, Server

logger = logging.getLogger('condottieri_common.models')

class ServerTestCase(TestCase):

    def test_no_server_error(self):
        with patch.object(logger, 'error') as mock_error:
            outdate_ranking(None)
            mock_error.assert_called_once_with("No configured server")

    def test_ranking_properly_outdated(self):
        Server.objects.create(ranking_last_update=datetime.now())
        outdate_ranking(None)
        server = Server.objects.get()
        self.assertEqual(server.ranking_outdated, True)

    def test_multiple_server_error(self):
        Server.objects.create(ranking_last_update=datetime.now())
        Server.objects.create(ranking_last_update=datetime.now())
        with patch.object(logger, 'error') as mock_error:
            outdate_ranking(None)
            mock_error.assert_called_once_with("Multiple servers found")

    def test_server_name(self):
        server = Server.objects.create(ranking_last_update=datetime.now())
        self.assertEqual(str(server), "Server %s" % (server.pk))
