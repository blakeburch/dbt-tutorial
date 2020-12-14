import subprocess
import os

dbt_command = os.environ.get('DBT_COMMAND')
subprocess.run([pwd])
subprocess.run(dbt_command.split(' '))
