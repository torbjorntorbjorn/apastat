from unittest import TestCase

from .test_data import document_single_worker, document_multiple_workers
from apastat.parser import parse


class TestParser(TestCase):
    def setUp(self):
        # We do most tests against single worker doc
        self.status = parse(document_single_worker)

    def test_single_worker(self):
        # Only one active worker
        self.assertEqual(len(self.status.active_workers), 1)

        # 14 workers in total
        self.assertEqual(len(self.status.workers), 14)

    def test_multiple_workers(self):
        status = parse(document_multiple_workers)

        # Only one active worker
        self.assertEqual(len(status.active_workers), 8)

        # 14 workers in total
        self.assertEqual(len(status.workers), 73)

    # From the stats table at the top of the document
    def test_current_time(self):
        self.assertEqual(self.status.current_time,
            'Thursday, 14-Jun-2012 22:36:43 CEST')

    # From the stats table at the top of the document
    def test_restart_time(self):
        self.assertEqual(self.status.restart_time,
            'Monday, 16-Apr-2012 10:49:27 CEST')

    # From the stats table at the top of the document
    def test_parent_server_generation(self):
        self.assertEqual(self.status.parent_server_generation, '22')

    # From the stats table at the top of the document
    def test_server_uptime(self):
        self.assertEqual(self.status.server_uptime,
            '59 days 11 hours 47 minutes 15 seconds')

    # From the stats table at the top of the document
    def test_total_accesses(self):
        self.assertEqual(self.status.total_accesses, '3266')

    # From the stats table at the top of the document
    def test_requests_currently_processed(self):
        self.assertEqual(self.status.requests_being_processed, '1')

    # From the stats table at the top of the document
    def test_idle_worker(self):
        self.assertEqual(self.status.idle_workers, '7')
