a=[1,2,3,4,5,6,7,8]
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print("even:",b)
print("odd:",c)
