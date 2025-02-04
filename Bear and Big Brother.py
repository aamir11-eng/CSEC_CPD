a,b=map(int,input().split())
n=0
if a==b:
    print(1)
else:
     while a<=b:
          n+=1
          a*=3
          b*=2
     print(n)
