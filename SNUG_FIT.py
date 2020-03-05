# Problem Name: School of Geometry
# Problem Code: SNUG_FIT
inp = int(input())
#S=0
while (inp>0):
    inp = inp-1
    S = 0
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A.sort()
    A.reverse()
    B.sort()
    B.reverse()

    for x in range(0,N):
        if A[x] >= B[x]:
            S = S+B[x]
        else:
            S = S+A[x]
    print(S)
