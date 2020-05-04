import os

GRAFANA_URL = os.getenv('GRAFANA_URL', 'https://grafana.falconxdev.com')
TOKEN = os.getenv('GRAFANA_TOKEN', 'eyJrIjoiNmNlRU02aWJOZzJtZ2FwSFhpY3ZWUzdTZFk2SjRMSXAiLCJuIjoiR3JhZmFuYSBSZWFkIE9ubHkiLCJpZCI6MX0=')

EXTRA_HEADERS = dict(h.split(':') for h in os.getenv('GRAFANA_HEADERS', '').split(',') if 'GRAFANA_HEADERS' in os.environ)

HTTP_GET_HEADERS = {'Authorization': 'Bearer ' + TOKEN}
HTTP_POST_HEADERS = {'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/json'}
for k,v in EXTRA_HEADERS.items():
    HTTP_GET_HEADERS.update({k: v})
    HTTP_POST_HEADERS.update({k: v})

SEARCH_API_LIMIT = 5000
DEBUG = True
VERIFY_SSL = False
