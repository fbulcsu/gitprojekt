karakter = str(input("Adj meg egy karakter sorozatot")) 
hossza = len(karakter)
nulla = 0 
for i in range (hossza): 
    for j in range(i + 1): 
        print(karakter[j], end=" ")
    for j in range(hossza-i-1):
        print(karakter[j], end=" ")
    print("")
for i in range (hossza):
    for j in range(hossza-i-1):
        print(karakter[j], end=" ")
    print("")