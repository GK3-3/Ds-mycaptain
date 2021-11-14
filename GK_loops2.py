n1=int(input("Enter the length of loop1 : "))
l1=[]
for i in range(n1):
    a=int(input("Enter the number : "))
    l1.append(a)
    if a<0:
        l1.remove(a)
print(l1)
