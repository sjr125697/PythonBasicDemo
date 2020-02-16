n = int(input())
for i in range(1, n+1):
    d=0
    for j in range(n-i): # 0 1 2 3 4
        print("%-3d" % (i+d,), end='')
        d+= (n-j)
    print("%d" % (i+d,))