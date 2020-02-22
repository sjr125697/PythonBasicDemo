s=int(input())
a=input().split()
b=input().split()
l=len(a)
a=[int(x) for x in a]
b=[int(x) for x in b]
c=[]
k=0
for i in range(l):
    c.append(a[i]+b[i])
for i in range(s):
    for j in range(s):
        print("{:2d}".format(c[k]),end=" ")
        k+=1
    print("")
