import math


def kivalaszt():
    n = int(input("\tSzám:"))
    prim = True
    if n < 2:
        prim = False
    else:
        i = 2
        while i <= math.sqrt(n) and n % i != 0:
            #osztja e maradékosan
            i = i+1
        prim = i > math.sqrt(n)
    if prim:
        print(f"{n} Prímszám")
    else:
        print(f"{n} Nem Prímszám")
