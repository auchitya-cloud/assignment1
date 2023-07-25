#original dictionary
D={1:5.6,2:7.8,3:6.6,4:8.7,5:7.7}
print("The original dictionary is: ",D)

#removing key=2
del D[2]
print("After removing key=2 :",D)

#to check if a key is present in D
key=D.keys()
if 6 in key:
    print("6 is a key in D")
else:
    print("6 is not a key in D.")

#count the number of elements in D
elements=len(D)
print("The number of elements in D is: ",elements)

#add all the values in D
val=D.values()
sum =0
for i in val:
    sum+=i
print("The sum of all values in D is: ",sum)

#update a value
D[3]=7.1
print("The updated dictionary is: ",D)

#clear the dictionary
D.clear()
print("D: ",D)
