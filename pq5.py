import random

L1=[]
L2=[]
for i in range (10):
    L1.append(random.randrange(10,30))
    L2.append(random.randrange(10,30))
    
print("L1 :",L1)
print("L2 :",L2)

#finding common elements between the lists
l=[]
for i in L1:
    if i in L2:
        if i not in l:
            l.append(i)
if(len(l)==0):
    print("There are no common elements in the two lists.")
else: 
    print("The common elements in the two lists are: ",l)


#finding cunique elements in the lists
print("The unique elements of L1 are: ")
for i in L1:
    if i not in L2:
        print(i, end=" ")
print("\nThe unique elements of L2 are: ")
for i in L2:
    if i not in L1:
        print(i, end=" ")

#finding max in both the lists
print("\nThe maximum element in L1 is: ",max(L1))
print("The maximum element in L2 is: ",max(L2))

#finding min in both the lists
print("The minimum element in L1 is: ",min(L1))
print("The minimum element in L2 is: ",min(L2))

#sum of both the lists
res_list=[]
for i in range(0,len(L1)):
    res_list.append((L1[i]+L2[i]))
print("The sum of two lists is: ", res_list)