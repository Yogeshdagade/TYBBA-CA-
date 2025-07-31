t=(1,2,3,4,5,3,4,6,8,9,7,8,0,5,0)
print(t)
l=[]
print("Repeated elements in given tuple")
for i in range(0,len(t)):
    if t.count(t[i])>1:
        if t[i] not in l:
            l.append(t[i])
            print(t[i])