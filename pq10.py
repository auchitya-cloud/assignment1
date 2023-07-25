#opening a file in write mode
f=open("demofile4.txt","w")

for number in range (600, 801):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            f.write(str(number)+" ")
f.close()

#reading contents of file
f=open("demofile4.txt","r")
print(f.read())
f.close()