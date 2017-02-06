#Proyecto final/Sleeping Queens
#Ulises Bruno Lozano
#04/02/2017
#Para correr el programa se tiene que pegar 

import random
import math

print "Bienvenido al juego Sleeping Queens.\n"
print "Objetivo:\n"
print "     El objetivo del juego es despertar a 4 reinas o llegar a 40 puntos:\n"
print "  \n"
print "Reglas: \n"
print "      Reyes: Tienen el poder de despertar una reina durmiente.\n"
print "      Caballeros: Roban una reina de tu oponente.\n"
print "      Dragones: Enfrentan a los caballeros evitando que roben una de tus reinas.\n"
print "      Pociones de dormir:  Pone a dormir una reina de tu oponente.\n"
print "      Varitas mágicas:  Te defiende de la Poción de Dormir.\n "
print "  \n"
print "Instrucciones:\n"
print " -Al comenzar se reparten 5 cartas a cada jugador.\n"
print " -Para realizar una jugada, tienes que introducir el siguiente comando: \n"
print "             jugada(1)\n"
print "     A continuacion introducir la carta que deseas jugar.\n"
print "     En caso de jugar un numero, se te pedira ingresar la operacion matematica;\n"
print "       que deseas aprovechar (suma, par o individual)\n"
print "       en caso de elegir la suma, deberas ingresar las dos cartas que deseas sumar\n"
print "       y la carta que sea igual a la suma, junto a aquellas dos, seran descartadas.\n"
print "       En caso de que elijas la operacion par, las dos cartas de tu mano se descartaran\n"
print " -En caso de que desees DESCARTAR directamente una carta, debes usar el comando:\n"
print "                 descartar(1)\n"
print "\n"
print " Recuerda, no juegas solo. El jugador 2, <<La Maquina>> hara su jugada inmediatamente despues"
print " de que tu hagas la tuya. Asi pues, estate atento a las puntuaciones\n"



reinas1=["Reina Arcoiris","Reina Pastel","Reina Estrella de mar","Reina Rosa"]
five=[5 for i in range(1,len(reinas1)+1)]
reinasfive=zip(reinas1,five)
reinas2=["Reina Mariquita","Reina Girasol","Reina Pavo Real", "Reina Luna"]
ten=[10 for i in range(1,len(reinas2)+1)]
reinasten=zip(reinas2,ten)
reinas3=["Reina Gato","Reina Perro","Reina Panqueque"]
fifteen=[15 for i in range(1,len(reinas2)+1)]
reinasfifteen=zip(reinas3,fifteen)
reinas4=["Reina Corazon"]
twenty=[20 for i in range(1,len(reinas2)+1)]
reinastwenty=zip(reinas4,twenty)
reyes=["Rey Odio","Rey Amor","Rey Enfermedad","Rey Salud","Rey Fuerza","Rey Fragilidad","Rey Guerra","Rey Muerte"]
caballeros=["Caballero Batalla","Caballero Herido","Caballero Venganza","Caballero Rencor"]
dragones=["Dragon Vanidad","Dragon Miedo","Dragon Orgullo"]
pociones=["Pocion del Dogma","Pocion de la Paz","Pocion de la Satisfaccion","Pocion del Placer"]
varitas=["Varita de la Templanza","Varita de la Prudencia","Varita del Silencio"]
bufones=["Bufon","Bufon","Bufon","Bufon","Bufon"]
numeros1=range(1,11)
numeros2=range(1,11)
numeros3=range(1,11)
numeros4=range(1,11)
numeros=numeros1+numeros2+numeros3+numeros4

len(bufones+varitas+dragones+caballeros+reyes+numeros+reinas1+reinas2+reinas3+reinas4+pociones)

random.shuffle(reinas1)
random.shuffle(reinas2)
random.shuffle(reinas3)
random.shuffle(reinas4)
random.shuffle(bufones)
random.shuffle(varitas)
random.shuffle(dragones)
random.shuffle(caballeros)
random.shuffle(reyes)
random.shuffle(numeros)
random.shuffle(pociones)

baraja=[]
reinas=reinasfive+reinasten+reinasfifteen+reinastwenty
reinasabsolute=reinasfive+reinasten+reinasfifteen+reinastwenty

for i in range(len(bufones)-1):
    baraja.append(bufones[i])
for i in range(len(varitas)-1):
    baraja.append(varitas[i])
for i in range(len(dragones)-1):
    baraja.append(dragones[i])
for i in range(len(caballeros)-1):
    baraja.append(caballeros[i])
for i in range(len(reyes)-1):
    baraja.append(reyes[i])
for i in range(len(numeros)-1):
    baraja.append(numeros[i])
for i in range(len(pociones)-1):
    baraja.append(pociones[i])

player1=raw_input("Introduce un seudonimo para jugar: ")
player2='Maquina'
cartasjugador1=[]
cartasjugador2=[]
descargue=[]

class jugador1():
    def __init__(self):
        self.puntuacion1= ""

class jugador2():
    def __init__(self):
        self.puntuacion2= ""

jugador1.puntuacion1=0
jugador2.puntuacion2=0

for i in range(5):
    cartasjugador1.append(random.choice(baraja))
    cartasjugador2.append(random.choice(baraja))
for i in cartasjugador1:
    baraja.remove(i)
for i in cartasjugador2:
    baraja.remove(i)

tlj=cartasjugador1
tlk="Esta es tu mano inicial "
tlo=player1
tlx=": "
tle="Tu mano nueva es: "
puntajep1=0
puntajep2=0

print repr(tlk) + tlo + repr(tlx) + repr(tlj)

len(bufones+varitas+dragones+caballeros+reyes+numeros+reinas1+reinas2+reinas3+reinas4+pociones)

def suma(x):
    a=input("Introduce una de las cartas de la Suma: ")
    b=input("Introduce otra de las cartas de la Suma: ")
    c=a+b
    if c in cartasjugador1:
        cartasjugador1.remove(a)
        cartasjugador1.remove(b)
        cartasjugador1.remove(c)
        descargue.append(a)
        descargue.append(b)
        descargue.append(c)
        k10=random.choice(baraja)
        k11=random.choice(baraja)
        k12=random.choice(baraja)
        baraja.remove(k10)
        baraja.remove(k11)
        baraja.remove(k12)
        cartasjugador1.append(k10)
        cartasjugador1.append(k11)
        cartasjugador1.append(k12)
    else:
        print 'Error. No hay una carta igual a la suma de esas dos cartas en tu mano.'
def par(x):
    b=input("Introduce el numero del par que deseas descartar: ")
    for i in cartasjugador1:
        if i==b:
            k20=random.choice(baraja)
            k25=random.choice(baraja)
            baraja.remove(k20)
            baraja.remove(k25)
            cartasjugador1.remove(i)
            cartasjugador1.remove(b)
            descargue.append(i)
            descargue.append(b)
            cartasjugador1.append(k20)
            cartasjugador1.append(k25)
            break
        else:
            print " "

def descartar(x):
    x=raw_input("Introduce la carta que deseas descartar directamente: ")
    cartasjugador1.remove(x)
    descargue.append(x)
    ey=random.choice(baraja)
    baraja.remove(ey)
    cartasjugador1.append(ey)
    print cartasjugador1


def individual(o):
    x=input("Introuce de nuevo la carta numero que quieres descartar: ")
    k19=random.choice(baraja)
    baraja.remove(k19)
    descargue.append(x)
    cartasjugador1.append(k19)
    cartasjugador1.remove(x)

def jugada(x):
    x=raw_input("¿Cuales cartas deseas jugar? ")

    if x in reyes:
        k=random.choice(reinas)
        cartasjugador1.remove(x)
        descargue.append(x)
        reinas.remove(k)
        cartasjugador1.append(k)
        jugador1.puntuacion1=jugador1.puntuacion1+k[1]
    elif x in bufones:
        cartasjugador1.remove(x)
        k1=random.choice(baraja)
        baraja.remove(k1)
        descargue.append(x)
        if k1 in numeros and k1%2==0:
            k7=random.choice(reinas)
            reinas.remove(k7)
            cartasjugador2.append(k7)
            jugador2.puntuacion2=jugador2.puntuacion2+k7[1]
        else:
            cartasjugador1.append(k1)
    elif x in pociones:
        for i in cartasjugador2:
            if i in varitas:
                k6=random.choice(baraja)
                cartasjugador2.remove(i)
                reinas.append(i)
                cartasjugador2.append(k6)
                baraja.remove(k6)
                cartasjugador1.remove(x)
                descargue.append(x)
                break
            elif i in reinasabsolute:
                cartasjugador2.remove(i)
                cartasjugador1.append(i)
                cartasjugador1.remove(x)
                descargue.append(x)
                jugador2.puntuacion2=jugador2.puntuacion2-i[1]
                jugador1.puntuacion1=jugador1.puntuacion1+i[1]

    elif x in caballeros:
        for r in cartasjugador2:
            if r in dragones:
                k3=random.choice(baraja)
                cartasjugador1.remove(x)
                descargue.append(x)
                cartasjugador1.append(k3)
                baraja.remove(k3)
                print "El jugador 2 tiene un Dragon en su mano."
            elif r in reinasabsolute:
                e=r
                k4=random.choice(baraja)
                cartasjugador2.remove(e)
                descargue.append(x)
                baraja.remove(k4)
                cartasjugador1.remove(x)
                cartasjugador2.append(k4)
                cartasjugador1.append(e)
                jugador1.puntuacion1=jugador1.puntuacion1+e[1]
                jugador2.puntuacion2=jugador2.puntuacion2-e[1]

    elif int(x) in numeros:
        tec=raw_input("Introduce la operacion que deseas aprovechar (suma, par o individual): ")
        if tec=='suma':
            suma(1)
        elif tec=='par':
            par(1)
        elif tec=='individual':
            individual(1)
    tli=cartasjugador1
    print tle+ repr(tli)
    print jugador1.puntuacion1
    print jugador2.puntuacion2

    jugadarandom=random.choice(cartasjugador2)

    if jugadarandom in reinas:
        jugadarandom=random.choice(cartasjugador2)
    if jugadarandom in reyes:
            k=random.choice(reinas)
            cartasjugador2.remove(jugadarandom)
            descargue.append(jugadarandom)
            reinas.remove(k)
            cartasjugador2.append(k)
            jugador2.puntuacion2=jugador2.puntuacion2+k[1]

    if jugadarandom in bufones:
        cartasjugador2.remove(jugadarandom)
        k1=random.choice(baraja)
        baraja.remove(k1)
        descargue.append(jugadarandom)
        if k1 in numeros and k1%2==0:
            k7=random.choice(reinas)
            reinas.remove(k7)
            cartasjugador1.append(k7)
            jugador1.puntuacion1=jugador1.puntuacion1+k7[1]
        else:
            cartasjugador2.append(k1)
    elif jugadarandom in pociones:
        for i in cartasjugador1:
            if i in varitas:
                k6=random.choice(baraja)
                cartasjugador1.remove(i)
                reinas.append(i)
                cartasjugador1.append(k6)
                baraja.remove(k6)
                cartasjugador2.remove(jugadarandom)
                descargue.append(jugadarandom)
            elif i in reinasabsolute:
                k88=i 
                cartasjugador1.remove(k88)
                cartasjugador2.append(k88)
                cartasjugador2.remove(jugadarandom)
                descargue.append(jugadarandom)
                jugador2.puntuacion1=jugador1.puntuacion1-k88[1]
                jugador1.puntuacion2=jugador2.puntuacion2+k88[1]

    elif jugadarandom in caballeros:
        for i in cartasjugador1:
            if i in dragones:
                k3=random.choice(baraja)
                cartasjugador2.remove(jugadarandom)
                descargue.append(jugadarandom)
                cartasjugador2.append(k3)
                baraja.remove(k3)
            elif i in reinasabsolute:
                e=i
                k4=random.choice(baraja)
                cartasjugador1.remove(e)
                descargue.append(jugadarandom)
                baraja.remove(k4)
                cartasjugador2.remove(jugadarandom)
                cartasjugador1.append(k4)
                cartasjugador2.append(e)
                jugador2.puntuacion2=jugador2.puntuacion2+e[1]
                jugador1.puntuacion1=jugador1.puntuacion1-e[1]

    else:
            k19=random.choice(baraja)
            baraja.remove(k19)
            descargue.append(jugadarandom)
            cartasjugador2.append(k19)
            cartasjugador2.remove(jugadarandom)

    if len(cartasjugador2)<5:
        buger=random.choice(baraja)
        baraja.remove(buger)
        cartasjugador2.append(buger)
    if len(cartasjugador1)<5:
        buger2=random.choice(baraja)
        baraja.remove(buger2)
        cartasjugador1.append(buger2)
    if len(baraja)<1:
        for i in descargue:
            baraja.append(i)

    if jugador1.puntuacion1>=40:
        print "EL JUGADOR 1 GANO"
    for i in cartasjugador1:
        pr=0
        if i in reinas:
            pr=pr+1
            return pr
        if pr>=4:
            print "EL JUGADOR 1 GANO"
    if jugador2.puntuacion2>=40:
        print "EL JUGADOR 2 GANO"
    for i in cartasjugador2:
        pr=0
        if i in reinas:
            pr=pr+1
            return pr
        if pr>=4:
            print "EL JUGADOR 2 GANO"
