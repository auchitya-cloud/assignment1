#creating dictionary
D={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}

#Writing to the file
f = open("demofile.txt", "w")
for key in D:
    f.write(str(key)+" ")
    f.write(str(D[key])+"\n")
f.close()

#open and read the file:
f = open("demofile.txt", "r")
for line in (f.readlines()):
    print(line)
f.close()