n = int(input())
lo = ([int(n) for n in input().split()])
lo.sort()
for i in range(0,4):
    num1 = lo.pop(-1)
    lo.reverse()
sum = 0
for j in range(len(lo)):
    sum += lo[j]
li = sum / len(lo)
print("aver={:.2f}".format(li))