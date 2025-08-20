check_str="yogeshbalasahebdagade"
dict={}
for i in check_str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for j in dict:
    print(j,"-",dict[j])