#creating list
L=["One","Two","Three","Four","Five"]

#writing to the file
f=open("demofile2.txt","w")
for i in L:
    size=len(i)
    f.write(i+",")
    f.write(str(size)+"\n")
f.close()

#reading from the file
f=open("demofile2.txt","r")
for line in (f.readlines()):
    print(line)
f.close()