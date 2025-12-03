import os
import requests
import json
from .config import OPENAI_API_KEY, LLM_ENDPOINT




class AIClient:
def __init__(self):
self.session = [] # conversation history in simple form


def ask(self, prompt: str) -> str:
# Primary: OpenAI API
if OPENAI_API_KEY:
return self._ask_openai(prompt)
elif LLM_ENDPOINT:
return self._ask_local(prompt)
else:
return "I'm not configured with an API key or local LLM."


def _ask_openai(self, prompt: str) -> str:
import openai
openai.api_key = OPENAI_API_KEY
messages = [
{"role": "system", "content": "You are a helpful assistant named Jarvis that can control a PC."}
]
for m in self.session:
messages.append(m)
messages.append({"role": "user", "content": prompt})
resp = openai.ChatCompletion.create(model='gpt-4o-mini', messages=messages, max_tokens=400)
text = resp['choices'][0]['message']['content']
self.session.append({"role": "user", "content": prompt})
self.session.append({"role": "assistant", "content": text})
return text


def _ask_local(self, prompt: str) -> str:
payload = {"prompt": prompt}
r = requests.post(LLM_ENDPOINT + '/v1/complete', json=payload)
return r.json().get('text','')
