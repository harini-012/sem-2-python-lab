sentence=input("Enter the sentence to count upper and lowercase letter")
upper=[]
lower=[]
u_c=0
l_c=0
def split():
    for i in  sentence:
        if i.isupper()==True:
            upper.append(i)
       
        if i.islower()==True:
            lower.append(i)
split()
for i in upper:
    u_c+=1
print(u_c)
for i in lower:
    l_c+=1
print(l_c)




