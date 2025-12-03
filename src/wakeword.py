"""Wake-word module. Uses pvporcupine if available; otherwise simple keyboard 'ctrl+shift+j' hotkey.
import threading
import keyboard




def on_wake_detected():
# placeholder for callback binding
pass




class WakeListener:
def __init__(self, callback, wakeword='jarvis'):
self.callback = callback
self.wakeword = wakeword
self.running = False
self.thread = None


def start(self):
self.running = True
if PV_AVAILABLE:
self.thread = threading.Thread(target=self._pv_listen, daemon=True)
else:
self.thread = threading.Thread(target=self._hotkey_listen, daemon=True)
self.thread.start()


def stop(self):
self.running = False


def _hotkey_listen(self):
# fallback: press ctrl+shift+j to wake
keyboard.add_hotkey('ctrl+shift+j', lambda: self.callback())
while self.running:
sd.sleep(1000)


def _pv_listen(self):
porcupine = pvporcupine.create(keywords=[self.wakeword])
device_info = sd.query_devices(kind='input')
samplerate = int(device_info['default_samplerate'])
with sd.InputStream(channels=1, samplerate=samplerate, dtype='int16') as stream:
while self.running:
pcm = stream.read(porcupine.frame_length)[0]
keyword_index = porcupine.process(pcm)
if keyword_index >= 0:
self.callback()




if __name__ == "__main__":
def cb():
print('Wake!')
w = WakeListener(cb)
w.start()
import time
time.sleep(10)
