# fibanocci series
num_terms=int(input())
n1=0
n2=1
count=0
if num_terms<=0:
    print("Enter a positive number")
elif num_terms==1:
    print (n1)
else:
    while count<num_terms:
        print(n1,end=" ")
        n3=n1+n2 
        n1=n2
        n2=n3
        count+=1
