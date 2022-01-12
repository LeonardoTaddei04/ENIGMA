
numero_degli_scambi=10
scambio=[]

r1=[3,24,0,6,7,4,12,17,11,23,21,15,18,19,16,14,1,20,8,13,5,9,25,2,10,22]
r2=[9,16,0,2,7,25,17,1,24,8,6,22,18,12,4,20,19,11,23,3,13,5,14,10,21,15]
r3=[21,5,16,19,6,1,17,4,22,8,23,7,15,3,20,25,2,9,18,10,24,0,14,12,11,13]
r4=[25,20,22,24,21,12,23,19,9,17,3,11,4,5,2,8,16,6,1,15,13,10,0,18,14,72]
r5=[1,23,21,18,14,13,4,3,11,22,9,8,12,16,19,20,0,2,24,25,17,15,10,7,5,6]
all_rot=[r1, r2, r3, r4, r5]

rif=[1,0,3,2,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18,21,20,23,22,25,24]

#funzione per lo scatto del rotori
#fa avanzare il rotore di 1 posizione
def scatto(r):
    scatto_rot=r.pop(0)
    r.append(scatto_rot)
    return (r)

#funzione che gira il rotore fino alla lettera inserita dall'utente
def giri_rot(r, c):
    while(chr(r[0]+ord("A"))!=c):
        r=scatto(r)
    return(r)


#funzione cha utilizza la funzione scatto 
#e se utile va ad utilizzare gli altri rotori
def scatto_rot(scatti_rot, passo1, passo2, rot1, rot2, rot3):
    rot1=scatto(rot1)
    if(scatti_rot % passo1==0):
        r2=scatto(rot1)
        if(scatti_rot % (passo1*passo2)==0):
            rot3=scatto(rot3)
    return(rot1, rot2, rot3)

#funzione che serve ad impostare i rotori
#-la sequenza dei rotori
#-lettera iniziale
def impostazione_rot(all_rot):
    r=int(input("INSERISCI ROTORE 1: "))
    rot1=all_rot[r-1]
    r=int(input("INSERISCI ROTORE 2: "))
    rot2=all_rot[r-1]
    r=int(input("INSERISCI ROTORE 3: "))
    rot3=all_rot[r-1]
    pos_rot1=input("INSERISCI LA POSIZIONE DI ROTORE 1:")
    pos_rot2=input("INSERISCI LA POSIZIONE DI ROTORE 2:")
    pos_rot3=input("INSERISCI LA POSIZIONE DI ROTORE 3:")
    rot1=giri_rot(rot1, pos_rot1)
    rot2=giri_rot(rot2, pos_rot2)
    rot3=giri_rot(rot3, pos_rot3)
    return (rot1, rot2, rot3)

#funzione che serve a fare lo scambio delle lettere inserite dall'utente
def impostazione_scambio(scambio):
    for i in range(26):
        scambio.append(i)
    for i in range(numero_degli_scambi):
        print("ESEMPIO AB SCAMBIA LA 'A' CON LA 'B' ")
        scambio_utente=input("INSERISCI LA LETTERA DA SCAMBIARE: ")
        scambio_lettera=scambio[ord(scambio_utente[0])-ord("A")]
        scambio[ord(scambio_utente[0])-ord("A")]=scambio[ord(scambio_utente[1])-ord("A")]
        scambio[ord(scambio_utente[1])-ord("A")]=scambio_lettera
    return(scambio)


rot1, rot2, rot3=impostazione_rot(all_rot)
scambio=impostazione_scambio(scambio)
passo1=int(input("INSERISCI PERIDO ROTORE 1: "))
passo2=int(input("INSERISCI PERIDO ROTORE 2: "))

print("INSERISCI LA PAROLA IN MAIUSCOLO (CAPS)")
parola_critto=input("INSERISCI LA PAROLA DA CRITTOGRAFARE: ")
scatti_rot=0

#VARIABILE che serve come contenitore della parola
contenitore_parola=""
for c in parola_critto:
    parola=ord(c)-ord('A')
    giro1=rif[rot3[rot2[rot1[scambio[parola]]]]]
    giro2=scambio.index(rot1.index(rot2.index(rot3.index(giro1))))
    parola=giro2+ord('A') 
    contenitore_parola=contenitore_parola+chr(parola) 
    scatti_rot+=1
    rot1, rot2, rot3=scatto_rot(scatti_rot, passo1, passo2, rot1, rot2, rot3) 
print("PAROLA CRITTOGRAFATA: ",contenitore_parola)






















