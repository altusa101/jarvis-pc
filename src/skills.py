from .utils import open_program, run_shell
import webbrowser
import os




def handle_command(text: str) -> str:
t = text.lower()
if 'open youtube' in t:
open_program('https://youtube.com')
return 'Opening YouTube.'
if 'open chrome' in t or 'open browser' in t:
open_program('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
return 'Opening Chrome.'
if 'shutdown' in t and 'computer' in t:
os.system('shutdown /s /t 5')
return 'Shutting down in 5 seconds.'
if 'what time' in t:
import time
return f'It is {time.strftime("%I:%M %p")}.'
# fallback: unknown
return ''
