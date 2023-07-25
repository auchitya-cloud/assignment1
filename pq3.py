#definig original sets
S1={10,20,30,40,50,60}
S2={40,50,60,70,80,90}
print("S1: ",S1)
print("S2: ",S2)

#adding elements in set
S1.update([55,66])
print("Updated S1: ",S1)

#removing elements
S1.remove(10)
S1.remove(30)
print("After removing elements: ",S1)

#checking the presence of an element in set
if 40 in S1:
    print("40 is present in S1")
else:
    print("40 is not present in S1")

#union of two sets
print("The union of S1 and S2 is: ",(S1|S2))

#intersection of two sets
print("The intersection of S1 and S2 is: ",(S1&S2))

#print s1-s2
print("The difference of S1 and S2 is: ",(S1-S2))