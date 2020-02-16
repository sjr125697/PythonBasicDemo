ss=input()
n=int(input())
c=input()

cnt= list(ss).count(c)
if cnt<n:
    print('no')
else:
    lt=ss.split(c)
    sum=0
    for i in range(n):
        sum+=len(lt[i])+1
    print(sum)