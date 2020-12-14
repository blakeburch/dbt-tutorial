import subprocess
import os

dbt_command = os.environ.get('DBT_COMMAND')
subprocess.run(dbt_command.split(' '))
