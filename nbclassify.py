import string
import math
import sys

def read():
	global dict3,dict1
	index=0
	file1 = open("nbmodel3.txt","r")
	for line in file1:
		if(index==0):
			dict3=eval(line)
		elif(index==1):
			dict1=eval(line)
		index+=1

read()
print (dict3)

exclude = set(string.punctuation)
prior_prob = [0,0,0,0]

#Calculate Prior Probability for each class
i=0
for k in dict1:
	prior_prob[i]=len(dict1[k])
	i+=1

#CLASSIFY PROGRAM
file3 = open(sys.argv[1],"r")
file=open("nboutput.txt",'w')
for line in file3:
	answer = [1,1,1,1]
	for i in line.split()[1:]:
		i = ''.join(ch for ch in i if ch not in exclude).lower()			#remove all punctuations and do lower case
		if i in dict3:
			#print (i,answer[0],dict3[i][0],total[0],"+++++++++")
			answer[0]=answer[0]+math.log(dict3[i][0])
			answer[1]=answer[1]+math.log(dict3[i][1])
			answer[2]=answer[2]+math.log(dict3[i][2])
			answer[3]=answer[3]+math.log(dict3[i][3])
	#print("ans  ",answer)
	#print (answer[0],prior_prob[0]/(sum(prior_prob))*1.0)
	#print ("---------------")
	answer[0]=answer[0]+math.log((prior_prob[0])/(sum(prior_prob)*1.0))
	answer[1]=answer[1]+math.log((prior_prob[1])/(sum(prior_prob)*1.0))
	answer[2]=answer[2]+math.log((prior_prob[2])/(sum(prior_prob)*1.0))
	answer[3]=answer[3]+math.log((prior_prob[3])/(sum(prior_prob)*1.0))
	#print(answer)
	#answer1 = list(map(int, answer))
	if answer[0] is max(answer):
		file.write(line.split()[0]+" "+"truthful positive"+"\n")
	elif answer[1] is max(answer):
		file.write(line.split()[0]+" "+"truthful negative"+"\n")
	elif answer[2] is max(answer):
		file.write(line.split()[0]+" "+"deceptive positive"+"\n")
	elif answer[3] is max(answer):
		file.write(line.split()[0]+" "+"deceptive negative"+"\n")

file.close()