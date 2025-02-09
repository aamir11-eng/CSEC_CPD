x=[1,2,3,4,5,6]
a,b=map(int,input().split())
c=0
for i in x:
    if i>=max(a,b):
        c+=1
m=len(x)
import math
gcd=math.gcd(c,m)
c//=gcd
m//=gcd
print(f"{c}/{m}")
