s=[1,2,1,3,0]

d=3
m=2
c=0
index=0

while(index<len(s) and index+m<=len(s)):
    
    sum=0
    for j in range(index,index+m):
        print(s[j])
        sum+=s[j]
    
    if sum==d:
        c+=1
    
    print("-----") 
    index+=1


    
print(c)
