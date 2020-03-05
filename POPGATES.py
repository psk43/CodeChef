# Problem Name: At the gates
# Problem Code: POPGATES
inp = int(input())
#count = 0
while(inp>0):
    inp = inp-1
    count=0
    N, K = map(int, input().split())
    Seq = input().split()

    for x in range(0,K):
        if Seq.pop() == 'H':
            for y in range(0,N-(x+1)):
                if Seq[y] == 'H':
                    Seq[y] = 'T'
                else:
                    Seq[y] = 'H'
        #print(Seq)

    for x in range(0,N-K):
        if Seq[x] == 'H':
            count = count+1

    print(count)
