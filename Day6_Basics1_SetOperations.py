a={1,3,4,5}
b={4,5,7,20,400}

union=a|b
print("Set Union:",union) #Union will combine and give all the values from both the sets as we learnt in school

intersect=a&b
print("Set Intersection:",intersect)

diference_a=a-b
print("Elements present in a but not in b:", diference_a)

diference_b=b-a
print("Elements present in b but not in a:", diference_b)

symmetric_differnece=a^b
print("Elements either present in a or b",symmetric_differnece)

symmetric_differnece_formula=(a-b)|(b-a)
print(symmetric_differnece_formula)


s1={20,40,30}
s1.add(50)
print(s1)

s1.add(50) #Even though we added 50, in the output two 50's were not present as sets have unique elements
print(s1)

s1.remove(50) #Removing 50 from the set
print(s1)

s1.remove(50)
print(s1) #Here we get an key error because 50 is not present in the set

s1.discard(40)
print(s1)

s1.discard(40)
print(s1) #Even though 40 is not present in the set it doesnt throws an error