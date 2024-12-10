#count the number of elements


even=[]
odd=[]
arr=[]
n=int(input("Enter the number of elements in the array"))
for i in range(n):
    e=int(input())
    arr.append(e)
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(len(odd))
print(len(even))

