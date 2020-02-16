a=input()
b=input()
x=len(a)
y=len(b)
c=-len(a)
d=-len(b)
if x>y:
    if a[d:]==b:
        print(b)
    else:
        print("no")
elif x<y:
    if a==b[c:]:
        print(a)
    else:
        print("no")
elif x==y:
    if a[c:]==b[c:]:
        print("all")
    else:
        print("no")
