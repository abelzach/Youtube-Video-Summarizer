import pyttsx3

text_speech = pyttsx3.init()

f = open("input.txt", "r")

res = f.read()

text_speech.say(res)
text_speech.runAndWait()