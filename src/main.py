python
from wakeword import WakeListener
from stt_vosk import record_and_transcribe
from tts_pyttsx3 import speak
from ai_client import AIClient
from skills import handle_command
from config import RECORD_SECONDS_LIMIT
import threading


ai = AIClient()




def on_wake():
print('Wake detected — listening...')
# record audio and transcribe
try:
text = record_and_transcribe(timeout=RECORD_SECONDS_LIMIT)
except Exception as e:
print('STT error:', e)
speak('Sorry, I had trouble hearing you.')
return
if not text or text.strip() == '':
speak('I did not hear anything.')
return
print('User said:', text)
# first try local skills
skill_resp = handle_command(text)
if skill_resp:
speak(skill_resp)
return
# otherwise ask AI for action or response
resp = ai.ask(f'User said: "{text}". If this is an actionable command for a PC, respond with: ACTION: <short description> or SPEAK: <response>. Only return one of the two formattings. Otherwise just give SPEAK: <response>.')
# parse response
if resp.startswith('ACTION:'):
# naive parsing — real system should use JSON
action = resp[len('ACTION:'):].strip()
# run shell for action (CAVEAT: no safety checks here)
run_shell(action)
speak('Action performed.')
elif resp.startswith('SPEAK:'):
out = resp[len('SPEAK:'):].strip()
speak(out)
else:
# default: speak entire response
speak(resp)




if __name__ == '__main__':
listener = WakeListener(on_wake)
listener.start()
print('Jarvis is running. Press ctrl+shift+j to wake (or use Porcupine).')
import time
try:
while True:
time.sleep(1)
except KeyboardInterrupt:
listener.stop()
print('Exiting...')
