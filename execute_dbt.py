import subprocess
import os
import json

dbt_command = os.environ.get('DBT_COMMAND', 'dbt run')

directory_of_file = os.path.dirname(os.path.realpath(__file__))
os.chdir(directory_of_file)

bigquery_credentials = os.environ.get('BIGQUERY_CREDS')
with open('bigquery_creds.json', 'w') as outfile:
    json.dump(bigquery_credentials, outfile)

subprocess.run(['sh', '-c', dbt_command])
