list=[2,4,3,3,1,3,2,1,3]

set1=set(list) #Removing the duplicates from a list the basic way
print(set1)

a=[1,2,3,5,6,3]
b=[21,4,1,3,5,66,6]
common=set(a)&set(b) #Finding common elements in a list
print(common)

list1=[20,40,50,20,30]
list2=[20,50,32,0,100]  
common1=set(list1)&set(list2)  
     
if common1:   #Checking if common elemnets in alist exists and printing them
    print("Common values exists which are: ", common1)
else:
    print("No common values exists in both lists")


text="programming"  
print(set(text)) #Printing the unique letters in a string using set

text2="He is a nice guy"

words=text2.lower().split()
unique_words=set(words)

print("Total unique words are: ", len(unique_words), "\n" "which are",unique_words )