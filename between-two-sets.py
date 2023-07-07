list1=[2,6]
list2=[24,36]

for i in range(1,1000):
    #partone
    fcheck=True
    scheck=True
    for j in list1:
        if i%j!=0:
            fcheck=False
            break
    

    for k in list2:
        if k%i!=0:
            scheck=False
    
    if fcheck and scheck:
        print(i)


