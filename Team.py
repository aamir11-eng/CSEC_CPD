x=int(input())
n=0
for i in range(x):
    a=[int(i) for i in input().split()]
    if sum(a)>=2:
        n+=1
print(n)
