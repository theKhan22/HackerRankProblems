def staircase(n):
    n2=n-1
    for i in range(n):
        output=""
        output+=(" "*n2)
        output+=("#"*(i+1))
        n2-=1
        print(output)

staircase(4)