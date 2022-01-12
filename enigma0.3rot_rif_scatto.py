rotore1 = [3, 24, 0, 6, 7, 4, 12, 17, 11, 23, 21, 15, 18, 19, 16, 14, 1, 20, 8, 13, 5, 9, 25, 2, 10, 22]
rotore2 = [3, 24, 0, 6, 7, 4, 12, 17, 11, 23, 21, 15, 18, 19, 16, 14, 1, 20, 8, 13, 5, 9, 25, 2, 10, 22]
rotore3 = [3, 24, 0, 6, 7, 4, 12, 17, 11, 23, 21, 15, 18, 19, 16, 14, 1, 20, 8, 13, 5, 9, 25, 2, 10, 22]
riflettore = [1,0,3,2,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18,21,20,23,22,25,24]

#FUNZIONE PER FAR AVANZARE IL ROTORE
def scatto(rotore):
    primogiro=rotore.pop(0)
    rotore.append(primogiro)
    return(rotore)

#FUNZIONE PER FAR FUNZIONARE GLI ALTRI ROTORI
def cambio_rotore(scatti, passoR1, passoR2, rotore1, rotore2, rotore3):
    rotore1=scatto(rotore1)
    if(scatti % passoR1==0):
        rotore2=scatto(rotore2)
        if(scatti % (passoR1*passoR2)==0):
            rotore3=scatto(rotore3)
    return(rotore1, rotore2, rotore3)      

parolacripto=input("Inserisci la parola che vuoi criptografare (MAIUSCOLO) : ")
passoR1=int (input("Inserisci il periodo del primo rotore: "))
passoR2=int (input("Inserisci il periodo del secondo rotore: "))

#
for c in parolacripto:
    parola=ord(c)-ord('A')
    primogiro=riflettore[rotore3[rotore2[rotore1[parola]]]]
    secondogiro=rotore1.index(rotore2.index(rotore3.index(primogiro)))
    parola=secondogiro+ord('A')
    scatti+=1
    rotore1, rotore2, rotore3=cambio_rotore(scatti, passoR1, passoR2, rotore1, rotore2, rotore3)
    print( chr(parola), end="")
