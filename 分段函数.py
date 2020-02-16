import math
x = float(input())
a= math.fabs(x)
if  a < 1:
    b=math.sqrt(2-2*x)
    print('f({:.3f})={:.3f}'.format(x,b))
elif x >= 1:
    d=2.5+(x+math.log(100))
    b=(math.cos(x)+math.pow(x,2))/d
    print('f({:.3f})={:.3f}'.format(x, b))
else:
    b=math.exp(x)
    print('f({:.3f})={:.3f}'.format(x, b))