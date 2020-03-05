# Problem Name: Tax Slabs
# Problem Code: SLAB
inp = int(input())
min = 250000
slab = [250000, 500000, 750000, 1000000, 1250000, 1500000]
slab_value = [0.05*250000, 0.10*250000, 0.15*250000, 0.20*250000, 0.25*250000, 0.30*250000]
while inp>0:
    inp = inp-1
    TI = int(input())

    if TI<250001:
        print(int((TI)))

    elif 250000 <= TI <= 500000:
        print(int(TI - 0.05*(TI-slab[0])))

    elif 500001 <= TI <= 750000:
        print(int(TI - 0.1*(TI-slab[1]) - slab_value[0]))

    elif 750001 <= TI <= 1000000:
        print(int(TI - 0.15*(TI-slab[2]) - slab_value[1] - slab_value[0]))

    elif 1000001 <= TI <= 1250000:
        print(int(TI - 0.20*(TI-slab[3]) - slab_value[2] - slab_value[1] - slab_value[0]))

    elif 1250001 <= TI <= 1500000:
        print(int(TI - 0.25*(TI-slab[4]) - slab_value[3] - slab_value[2] - slab_value[1] - slab_value[0]))

    else:
        print(int(TI - 0.3*(TI-slab[5]) - slab_value[4] - slab_value[3] - slab_value[2] - slab_value[1] - slab_value[0]))
