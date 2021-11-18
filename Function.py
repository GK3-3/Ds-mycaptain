s=input("Please Enter a string")
def most_frequent(string):
    l=[]
    for i in range(len(s)):
        l.append(s[i])
    se=set(l)
    l1=[]
    for i in se:
        l1.append(l.count(i))
    se1=set(l1)
    d={}
    l2=[]
    for j in se1:
        for i in se:
            if l.count(i)==j:
                l2.append(i)
                d[i]=l.count(i)
    l2.reverse()
    for i in l2:
        print(i,"=","%.2d" % d[i])
most_frequent(s)
