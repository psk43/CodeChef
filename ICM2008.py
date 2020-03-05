# Problem Name: Mr Pr in a dilemma
# Problem Code: ICM2008
inp = input()
while inp>0:
    a,b,c,d = map(int, input().split())
    dist = abs(a-b)
    speed = abs(c-d)

    if speed == 0:
        if dist == 0:
            print("YES")
            continue
        else:
            print("NO")
            continue

    if dist%speed == 0:
        print("YES")
    else:
        print("NO")
