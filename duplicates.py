a=[5,3,4,6,7,5,3,2,1]
ferq = {}
l=[]
for i in a:
    if i  in ferq:
        ferq[i]+=1
    else:
        ferq[i]=1
for i,j in ferq.items():
    if ferq[i]>1:
        l.append(i)
print(l)
m=0
for i in l:
        m+=i
print(m)

