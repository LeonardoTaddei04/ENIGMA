rotore1 = [3, 24, 0, 6, 7, 4, 12, 17, 11, 23, 21, 15, 18, 19, 16, 14, 1, 20, 8, 13, 5, 9, 25, 2, 10, 22]
rotore2 = [3, 24, 0, 6, 7, 4, 12, 17, 11, 23, 21, 15, 18, 19, 16, 14, 1, 20, 8, 13, 5, 9, 25, 2, 10, 22]
rotore3 = [3, 24, 0, 6, 7, 4, 12, 17, 11, 23, 21, 15, 18, 19, 16, 14, 1, 20, 8, 13, 5, 9, 25, 2, 10, 22]
riflettore=  [1,0,3,2,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18,21,20,23,22,25,24]

parolacripto=input("Inserisci la parola che vuoi criptografare (MAIUSCOLO) : ")
for c in parolacripto:
    parola=ord(c)-ord('A')
    primogiro=riflettore[rotore3[rotore2[rotore1[parola]]]]
    secondogiro=rotore1.index(rotore2.index(rotore3.index(primogiro)))
    parola=secondogiro+ord('A')
    print( chr(parola), end="")
print()
