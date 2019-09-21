from datetime import datetime

from django.test import TestCase

from condottieri_common.management.commands.update_weighted_scores import Command
from condottieri_common.models import Server

class CommandTestCase(TestCase):

    ##TODO: Create some fixtures to test game funcionality
    
    def setUp(self):
        self.server = Server.objects.create(ranking_last_update=datetime.now())

    def test_ranking_not_outdated(self):
        command = Command()
        self.assertIsNone(command.handle_noargs())
    
    def test_no_games(self):
        self.server.outdate_ranking()
        command = Command()
        self.assertIsNone(command.handle_noargs())
