lista = [5, 2, 4, 7, 3]

while True:
    change = False
    for l in range(len(lista) -1):
        if lista[l] > lista[l + 1]:
            lista[l], lista[l + 1] = lista[l + 1], lista[l]
            change = True
    
    if change == False:
        break
print(lista)


liczby = [2, 5, 7, 8, 3, 9]
print(f"Oto lista nieposortowana:{liczby}")

while True:
    babel = False
    for n in range(len(liczby) -1):
        if liczby[n] > liczby[n+1]:
            liczby[n], liczby[n+1] = liczby[n+1], liczby[n]
            babel = True
    if babel == False:
        break
print(f"A to posortowane już liczby: {liczby}")