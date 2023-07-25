#1. printing 100 random strings
import string
import random

size=[6,7,8]
print("The generated random strings are: ")
# using random.choices()
# generating random strings
for i in range (100):
    N=random.choice(size)
    res = ''.join(random.choices(string.ascii_letters, k=N))
 
    # print result
    print(str(res))


#2. Print prime numbers between 600 and 800
print("The prime numbers between 600 and 800 are: ")
for number in range (600, 801):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  

#3. Print numbers between 100 and 1000 that are divisible by 7 and 9
print("The numbers between 100 and 1000 that are divisible by 7 and 9 are: ")
for num in range(100,1001):
    if((num%7==0) and (num%9==0)):
        print(num)