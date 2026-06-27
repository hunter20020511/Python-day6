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