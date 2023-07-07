
ar=[1,3,2,6,1,2]
k=3
n=len(ar)
c=0
for i in range(n-1):
    for j in range(i+1,n):
                
        if (ar[i]+ar[j])%k==0:           
            c+=1
                
print(c)
               