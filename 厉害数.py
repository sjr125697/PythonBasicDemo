
n = int(input())
for h in range(1,10**(n)):
    um = 0
    while t!=0:
         i = h % 10
         t = int(t/10)
         um += i**(5)
    if um == h:
        print(um)