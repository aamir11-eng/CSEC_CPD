x=int(input())
l=[]
for i in range(x):
    y=input()
    l.append(y)
m=1
n=0
s=1
while m<=len(l)-1:
    if l[n]!=l[m]:
         s+=1
         m+=1
         n+=1
    else:
        m+=1
        n+=1
print(s)
