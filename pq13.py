#function to compute the average score of each student 
def solve(d):
    avg_scores = dict()
    for name in d:
      avg_scores[name] = sum(d[name])/len(d[name])
    return avg_scores

#creating a dictionary
d={'Student1':[53,87,56,69,77],'Student2':[97,83,91,78,88],'Student3':[41,56,49,65,52],'Student4':[69,78,91,66,75],'Student5':[35,42,47,51,47]}
print("The original dictionary is: ",d)
d2=solve(d)

#finding the maximum and minimum average marks
max_val=max(d2.values())
min_val=min(d2.values())

#displaying the students having maximum and minimum average marks
for key,value in d2.items():
   if (value==max_val):
      print(key,"has the maximum average marks = ",max_val)
   if (value==min_val):
      print(key,"has the minimum average marks = ",min_val)