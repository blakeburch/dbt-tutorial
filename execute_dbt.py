import subprocess
import os
import json

dbt_command = os.environ.get(
    'DBT_COMMAND',
    'dbt run')

bigquery_credentials = os.environ.get('BIGQUERY_CREDS')
bigquery_credentials = json.loads(bigquery_credentials)

directory_of_file = os.path.dirname(os.path.realpath(__file__))
os.chdir(directory_of_file)
with open('bigquery_creds.json', 'w') as outfile:
    json.dump(bigquery_credentials, outfile)


command = subprocess.run(['sh', '-c', dbt_command], capture_output=True)
sys.exit(command.returncode)
