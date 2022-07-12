from googletrans import Translator
f = open("t.txt", "r")
fin = f.read()
trans = Translator()
res = ""
a = fin.split(".")
for i in a :
    a = 'hi'
    out = trans.translate(i,  dest = a)
    res = res + str(out.text)
    res = res + ' . '
print(res)
