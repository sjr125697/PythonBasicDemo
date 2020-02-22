n = int(input())
h=1
for x in range(h, n+1):
    flag=0
    for g in range(n-x): 
        print("%-3d" % (flag+x), end='')
        flag+= (n-g)
    print("%d" % (flag+x))
