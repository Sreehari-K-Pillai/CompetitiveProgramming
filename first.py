def ThreeNplusOne(x):
    count=1
    while x!=1:
        if x%2==0:
            x=x/2
            count=count+1
        else:
            x=x*3+1
            count=count+1
    return count
x,y=input().split(' ')
x=int(x)
y=int(y)
max=ThreeNplusOne(x)
while x<=y:
    ele=ThreeNplusOne(x)
    x=x+1
    if max>=ele:
        max=max
    else:
        max=ele
print(max)