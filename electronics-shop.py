b,n,m = map(int,input().split())


keyboards=list(map(int, input().rstrip().split()))
drives=list(map(int, input().rstrip().split()))

max=-1

for i in range(n):
    for j in range(m):
        if keyboards[i]+drives[j]<=b and keyboards[i]+drives[j]>max:
            max=keyboards[i]+drives[j]

print(max)  