import string
import math
import sys


file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"r")

dict1 = {			#Key=Class : Value=IDs
    "TP" : [],
    "TN" : [],
    "DP" : [],
    "DN" : []
    }
dict2 = dict()			#key=ID : Value=Words in the review
dict3 = dict()			#Contains word count for each unique word for each class
total = [0,0,0,0]		#Total count for each class
exclude = set(string.punctuation)
#punct=punct.translate(None,"`-=[]\;'/?~!Q@#$%^&*()_:.+,")


for line in file2:
    if line.split()[1] == "truthful" and line.split()[2] == "positive":
        dict1["TP"].append(line.split()[0])
    elif line.split()[1] == "truthful" and line.split()[2] == "negative":
        dict1["TN"].append(line.split()[0])
    elif line.split()[1] == "deceptive" and line.split()[2] == "positive":
        dict1["DP"].append(line.split()[0])
    elif line.split()[1] == "deceptive" and line.split()[2] == "negative":
        dict1["DN"].append(line.split()[0])

		
for line in file1:
	for i in line.split()[1:]:
		i = ''.join(ch for ch in i if ch not in exclude).lower()		#remove all punctuations and do lower case
		if line.split()[0] in dict2:
			dict2[line.split()[0]].append(i)
		else:
			dict2[line.split()[0]] = [i]
	
"""file1.close	
file1 = open("train-text.txt","r")
for line in file1:
	for i in line.split()[1:]:
		if not i in uniquewords_count:
			uniquewords.append(i)"""

#Creating the word count table
for key in dict2:
	for word in dict2[key]:
		if word not in dict3 and any(char.isdigit() for char in word) is False:
			dict3[word]=[0,0,0,0]
			for k in dict1:
				if key in dict1[k]:
					if k is "TP":
						dict3[word]=[1,0,0,0]
					elif k is "TN":
						dict3[word]=[0,1,0,0]
					elif k is "DP":
						dict3[word]=[0,0,1,0]
					elif k is "DN":
						dict3[word]=[0,0,0,1]
		elif any(char.isdigit() for char in word) is False:
			for k in dict1:
				if key in dict1[k]:
					if k is "TP":
						dict3[word][0]=dict3[word][0]+1
					elif k is "TN":
						dict3[word][1]=dict3[word][1]+1
					elif k is "DP":
						dict3[word][2]=dict3[word][2]+1;
					elif k is "DN":
						dict3[word][3]=dict3[word][3]+1

#print(sorted(dict3.values(),reverse=True))
common_words=["a","the","is","was","were","that","their","should","can","could","must","they","their","get","got","put",
"keep","it","on","for","in","about","upon","you","i","we","would","and","will","number","be","he","she","it","their"
"that","ok","k","one","two","three","four","five","six","seven","eight","nine","up","down","us","but","all","where"
,"been","of","do","dont","later","make","made","ans","at","our","him","his","her","else","did","does","done","had"
"has","have","to","than","with","by","or","makes","likes","liked","made","kmow","my","from","went","told","only","this"
,"much","me","mine","im","say","said","spoke","men","women","since","back","before","okay","an","what","where","who","whom"
,"also","if","other","yet","go","such","throughout","through","though","as","when","oh","so","here","after","them","then",
"what","man","woman","there","let","now","bed","come","came","its","ill","ive","were""there","hyatt","regency","chicago","husband","summer","vacation",
"couldnt","had","some","seems","north","michigan","avenue","are","drake","westin","concierge","august","fiancee","city",
"even","while","see",""]

for k in common_words:
	if k in dict3:
		del dict3[k]

#Smoothing						
for k in dict3:						
	dict3[k][0]=dict3[k][0]+1
	dict3[k][1]=dict3[k][1]+1
	dict3[k][2]=dict3[k][2]+1
	dict3[k][3]=dict3[k][3]+1

#Calculate total count for each class + unique words (B)
for k in dict3:
	total[0]+=dict3[k][0]
	total[1]+=dict3[k][1]
	total[2]+=dict3[k][2]
	total[3]+=dict3[k][3]
"""total[0]+=len(dict3)
total[1]+=len(dict3)
total[2]+=len(dict3)
total[3]+=len(dict3)"""


"""for i in dict3:
	print(i,dict3[i])
sys.exit()"""

#Remove useless words from dict3 with 20% threshold
useless=[]
for k in dict3:
	t=max(dict3[k])-(max(dict3[k])*0.3)
	if (dict3[k][0]>t and dict3[k][1]>t and dict3[k][2]>t and dict3[k][3]>t):
		useless+=[k] 

for k in useless:
	if k in dict3:
		del dict3[k]


file4 = open("nbmodel3.txt","w")

for k in dict3:
	dict3[k][0]=dict3[k][0]/(total[0]*1.0)
	dict3[k][1]=dict3[k][1]/(total[1]*1.0)
	dict3[k][2]=dict3[k][2]/(total[2]*1.0)
	dict3[k][3]=dict3[k][3]/(total[3]*1.0)

file4.write(str(dict3)+"\n")
file4.write(str(dict1))
file4.close()

