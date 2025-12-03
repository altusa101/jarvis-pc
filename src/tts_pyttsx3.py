import pyttsx3


_engine = pyttsx3.init()
_engine.setProperty('rate', 170)




def speak(text: str):
_engine.say(text)
_engine.runAndWait()




if __name__ == '__main__':
speak('Hello. I am Jarvis. Ready when you are.')
