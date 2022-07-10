from googletrans import Translator

trans = Translator()
f = open("t.txt", "r")
tex = f.read()
a = 'es'
out = trans.translate(tex,  dest = a)
print(out.text)
