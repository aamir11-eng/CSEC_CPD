x=int(input())
y=[int(i) for i in input().split()]
h=0
ut=0
for i in y:
     if i>0:
        h+=i
     elif i<0 and h>0:
         h-=1
     elif i<0 and h<1:
         ut+=1
print(ut)
