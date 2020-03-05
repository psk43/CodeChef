# Problem Name: Peak Finding
# Problem Code  UWCOI20A
inp = int(input())
#print(inp)
while(inp>0):
    inp = inp-1
    N = int(input())
    #print('N=',N)
    peak = 0
    for x in range(0,N):
        p1 = int(input())
        #print('p1=',p1)
        if(p1>peak):
            peak=p1;
            #print('peak=',peak)

    print(peak)

