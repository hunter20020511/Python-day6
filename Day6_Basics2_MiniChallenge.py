##Count how many times each word appears in a sentence##

sentence="He is a nice guy but also a bad guy"
lowe_sent=sentence.lower().split()  #Normalizing the given sentence and splitting it word by word

counter={} #Initialising empty dict

for word in lowe_sent: #Looping over given sentece
    if word in counter:
        counter[word]+=1 #If word is found, then increasing the counter i.e empty set by 1
    else:
        counter[word]=1  #If word not found then simply addin the new word in the empty dictionary 
print(counter)  #Printing the result

