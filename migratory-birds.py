
def migratoryBirds(arr):
    n=len(arr)
    aux=[0]*(n+1)
    for i in arr:
        aux[i]+=1
    
    max=aux[0]
    ind=0
    print(aux)
    for i in range(n+1):
        if aux[i]>max:
            max=aux[i]
            ind=i

    print(ind)

    


n=int(input())

a=list(map(int, input().rstrip().split()))
print(a)


migratoryBirds(a)