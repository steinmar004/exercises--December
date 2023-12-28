ilosc_liczb = 20
lista_do_pomieszania = list(range(1,ilosc_liczb + 1))
l = lista_do_pomieszania
import random
for ab in range(ilosc_liczb*2):
    a = random.randint(0, ilosc_liczb-1)
    b = random.randint(0, ilosc_liczb-1)
    print(f"{a} {b}")
    l[a], l[b] = l[b], l[a]
print(l)  