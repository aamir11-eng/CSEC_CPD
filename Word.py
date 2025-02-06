y=input()
upper=0
lower=0
for i in y:
    if i==i.upper():
        upper+=1
    else:
        lower+=1

if upper>lower:
        print(y.upper())
else:
        print(y.lower())
