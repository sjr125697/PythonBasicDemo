d1=eval(input());d2=eval(input())
l1=[];l2=[]
pl={}
for i in d1:
    pl[i]=pl.get(i,0)+d1.get(i,0)
    if type(i)==type(1):
        l1.append(i)
    elif type(i)==type('w'):
        l2.append(i)
for i in d2:
    pl[i] = pl.get(i, 0) + d2.get(i, 0)
    if type(i)==type(1):
        l1.append(i)
    elif type(i)==type('w'):
        l2.append(i)
l1.sort();l2.sort()
list=l1+l2
print("{",end="")
cnt=0;length=len(pl)
for i in list:
    if i in pl:
        cnt += 1
        if type(i)==type(1):
            print("{}:{}".format(i,pl[i]),end="")
        else:
            print('"{}":{}'.format(i,pl[i]),end="")
        del pl[i]
        if cnt!=length:
            print(",",end="")
print("}")
