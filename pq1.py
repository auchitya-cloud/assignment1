from math import sqrt
#original list
L=[11,12,13,14]
print("Original list: ",L)

#appeding 50 and 60 to L
L.extend([50,60])
print("After appending: ",L)

#removing 11 and 13
rem=[11,13]
for i in L:
    if i in rem:
        L.remove(i)
print("After removing elements: ",L)

#sorting in ascending order
L.sort()
print("After sorting: ",L)

#sorting in descending order
L.sort(reverse=True)
print("After sorting: ",L)

#searching 13 in list
for i in L:
    if(i==13):
        print("Element found")
        break
else:
    print("Element not found.")

#Counting number of elements
num=0
for i in L:
    num+=1
print("Number of elememts in L are: ",num)

#finding sum of elements
sum=0
for i in L:
    sum=sum+i
print("Sum of all elements is: ",sum)

#finding sum of odd elements
sum=0
for i in L:
    if(i%2!=0):
        sum=sum+i
print("Sum of all odd elements is: ",sum)

#finding sum of even elements
sum=0
for i in L:
    if(i%2==0):
        sum=sum+i
print("Sum of all even elements is: ",sum)

#finding sum of prime elements
sum=0
prime_flag=0
for i in L:
    for n in range(2, int(sqrt(i)) + 1):
        if (i % n == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        sum=sum+1
print("Sum of all elements is: ",sum)

#clear all elements of L
L.clear()
print("After clearing L:",L)

#deleting L
del(L)
#print(L) displays error 'L not defined'
