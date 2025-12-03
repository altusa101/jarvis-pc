import time
import subprocess
import platform
import os




def open_program(path_or_command: str):
"""Cross-platform open program/URL."""
system = platform.system()
if system == 'Windows':
os.startfile(path_or_command)
elif system == 'Darwin':
subprocess.Popen(['open', path_or_command])
else:
subprocess.Popen(['xdg-open', path_or_command])




def run_shell(cmd: str):
return subprocess.Popen(cmd, shell=True)




def short_timestamp():
return time.strftime('%Y-%m-%d %H:%M:%S')
