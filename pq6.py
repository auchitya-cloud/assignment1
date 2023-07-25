import random

#creating lists
List=[]
for i in range (100):
    List.append(random.randrange(100,900))
print("The original list is: ",List)

#counting all the odd numbers
count_odd=0
print("Odd numbers in the list are: ")
for num in List:
    if(num%2!=0):
        count_odd+=1
        print(num, end=" ")
print("\nThe number of odd elements in the list are: ",count_odd)

#counting all the odd numbers
count_even=0
print("Even numbers in the list are: ")
for num in List:
    if(num%2==0):
        count_even+=1
        print(num, end=" ")
print("\nThe number of even elements in the list are: ",count_even)

#counting all the prime numbers in the list
count_prime=[]
print("The prime numbers in the list are: ")
for number in range (0,len(List)):
    if (number > 1 and number not in count_prime):  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            count_prime.append(number)
            print(number, end=" ") 
print("\nThe number of prime elements in the list are: ",len(count_prime))