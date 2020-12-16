import subprocess
import os
import json
import sys

# Follow these instructions to successfully set up this Blueprint:
instructions = """
1) Add the contents of this file to the root directory of the Github repository where your dbt models live, with the file name of "execute_dbt.py".
2) Move your profiles.yml file to the root directory of the Github repository where your dbt models live.
3) Connect Shipyard to the Github repository where your dbt models live.
4) Connect this Blueprint to the Github repository and branch/tag where your dbt models live.
5) If you used the default setting of cloning your Github repository to a folder with the repo's name, update the "File to Run" field to include the name of your repo as a folder. e.g. "your_repo_name/execute_dbt.py" If you opted to clone into the current working directory, do nothing.
6) Click "Use this Blueprint" to get started.
"""

bigquery_credentials = os.environ.get('BIGQUERY_CREDS')
directory_of_file = os.path.dirname(os.path.realpath(__file__))
dbt_command = os.environ.get('DBT_COMMAND', 'dbt run')

if os.path.realpath(__file__) == '/home/shipyard/execute_dbt.py':
    print('This dbt Blueprint is not set up properly. Edit this Blueprint and follow the instructions below:')
    print(instructions)
    sys.exit(1)
else:

    os.chdir(directory_of_file)
    if bigquery_credentials:
        bigquery_credentials = json.loads(bigquery_credentials)
        with open('bigquery_creds.json', 'w') as outfile:
            json.dump(bigquery_credentials, outfile)

    subprocess.run(['sh', '-c', dbt_command], check=True)
