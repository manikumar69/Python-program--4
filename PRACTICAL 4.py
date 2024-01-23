fh=open('prac4.txt','w')

abc=[1,2,3,4,5,6,7,8,9,10]
sum=0
i=0
while(i<len(abc)):
    sum= sum + abc[i]
    i=i+1
avg=int(sum/len(abc))
print('The average is:', avg)
fh.write('The average is '+ str(avg))
fh.close()