
n=int(input())
for i in range(1,10**n):
    j=i
    sum=0
    if i>194979:
        break
    while i!=0:
        a=i%10
        i=i//10
        sum+=a**5
    if sum==j:
        print(j)
