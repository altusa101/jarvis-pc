from dotenv import load_dotenv
import os


load_dotenv()


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
LLM_ENDPOINT = os.getenv('LLM_ENDPOINT')
WAKEWORD = os.getenv('WAKEWORD', 'jarvis')
VOICE_NAME = os.getenv('VOICE_NAME', 'Jarvis')
RECORD_SECONDS_LIMIT = 12 # max seconds to record after wakeword
