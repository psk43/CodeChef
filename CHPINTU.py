# cook your dish here
T = int(input())
while(T>0):
    T=T-1
    N, M = map(int, input().split())
    F = map(str, input().split())
    P = map(int, input().split())
    FP = list(zip(F,P))
    #print(FP)
    FP_Dict = {}

    for x in FP:
        try:
            FP_Dict[x[0]].append(x[1])
            #print(FP_Dict)
        except KeyError:
            FP_Dict[x[0]] = [x[1]]

    for key in FP_Dict:
        FP_Dict.update({key:sum(FP_Dict[key])})
        
    #print(FP_Dict)
    print(FP_Dict[min(FP_Dict, key=FP_Dict.get)])
    
