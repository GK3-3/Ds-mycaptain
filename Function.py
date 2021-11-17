s=input()
def most_frequent(string):
    l=[]
    for i in range(len(s)):
        l.append(s[i])
    se=set(l)
    for i in se:
        print(i,"=",l.count(i))
most_frequent(s)
