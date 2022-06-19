from gtts import gTTS

def makeMP3(words, mp3name, language="en", normal=True, tld="co.in"):
    tts = gTTS(text = words, lang = language)
    tts.save("%s.mp3" % mp3name)
    print("File %s.mp3 created" % mp3name)

f = open("input.txt", 'r')
text = f.read()

makeMP3(text, "english")