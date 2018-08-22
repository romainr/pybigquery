"""Integration with BigQuery API."""

from __future__ import absolute_import
from __future__ import unicode_literals

from google.cloud.bigquery import Client, QueryJobConfig


class ApiClient(object):
    def __init__(self, credentials_path=None):
        self.credentials_path = credentials_path
        if self.credentials_path:
            self.client = Client.from_service_account_json(
                self.credentials_path)
        else:
            self.client = Client()

    def dry_run_query(self, query):
        job_config = QueryJobConfig()
        job_config.dry_run = True
        job_config.use_query_cache = False
        return self.client.query(query=(query), job_config=job_config)
