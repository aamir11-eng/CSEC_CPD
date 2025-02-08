x=input()
s='a'
c=0
for i in x:
    m=abs(ord(s)-ord(i))
    n=26-abs(ord(s)-ord(i))
    c+=min(m,n)
    s=i
print(c)
