import string
import random

#opening a file and writing strings to it
f=open("demofile3.txt","w")
# using random.choices()
# generating random strings
for i in range (100):
    N=random.randrange(10,15)
    res = ''.join(random.choices(string.ascii_letters, k=N))
    f.write(res+"\n")
f.close()

#opening the file to read the content
f=open("demofile3.txt","r")
for line in (f.readlines()):
    print(line)
f.close()