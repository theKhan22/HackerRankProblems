
def bonAppetit(bill, k, b):
    sum=0
    n=len(bill)
    for i in range(n):
        if i!=k:
            sum+=bill[i]
    
    result=int(b-(sum/2))

    if result==0:
        print('Bon Appetit')
    else:
        print(result)



n,k=map(int,input().split())

bill=list(map(int,input().rstrip().split()))

b=int(input())

bonAppetit(bill,k,b)
