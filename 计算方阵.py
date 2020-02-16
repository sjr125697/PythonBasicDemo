
n=int("3")
a="1 2 3 4 5 6 7 8 9"
b="2 3 4 5 6 7 8 9 1"
a=a.split()
b=b.split()
for i in range(n):
    for j in range(n):
        sum=int(a[3*i+j])+int(b[3*i+j])
        if 10<=sum<=99:
            print("_" + str(sum),end=' ')
        elif 0<=sum<=9:
            print("__" + str(sum),end=' ')
    print()