# Vosk-based STT
import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer
import os


q = queue.Queue()


model = None




def ensure_model(path='model'):
global model
if model is None:
if not os.path.exists(path):
raise RuntimeError('Please download a Vosk model and place it in the "model" folder.')
model = Model(path)




def record_and_transcribe(timeout=12):
# record audio for `timeout` seconds and transcribe
ensure_model()
samplerate = 16000
device = None
with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16', channels=1) as stream:
rec = KaldiRecognizer(model, samplerate)
rec.SetWords(True)
import time
t0 = time.time()
while True:
data = stream.read(4000)[0]
if rec.AcceptWaveform(data):
res = rec.Result()
j = json.loads(res)
return j.get('text', '')
if time.time() - t0 > timeout:
res = rec.FinalResult()
j = json.loads(res)
return j.get('text', '')




if __name__ == '__main__':
print('Say something...')
print(record_and_transcribe(8))
