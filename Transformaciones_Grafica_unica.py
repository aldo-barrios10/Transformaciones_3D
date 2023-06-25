
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, CheckButtons 

def trasladar(vertices, listaT):
    aumX=0
    aumY=0
    for i in range(len(listaT)):
        aumX+=listaT[i][0]
        aumY+=listaT[i][1]

    for i in range(len(vertices)):
        vertices[i][0]= vertices[i][0] + aumX
        vertices[i][1]= vertices[i][1] + aumY

    return vertices

#SEPARA LOS ELEMENTOS EN X Y Y PARA PODER GRAFICAR
def acomodarVertices(vertices):
    listaX=[]
    listaY=[]
    for i in range(len(vertices)):
        listaX.append(vertices[i][0])
        listaY.append(vertices[i][1])

    listaX.append(vertices[0][0])
    listaY.append(vertices[0][1])

    return listaX,listaY

def escalar(vertices, listaE):
    escalaX=1
    escalaY=1

    for i in range(len(listaE)):
        escalaX*=listaE[i][0]
        escalaY*=listaE[i][1]

    for i in range(len(vertices)):
        vertices[i][0]= vertices[i][0] * escalaX
        vertices[i][1]= vertices[i][1] * escalaY
    
    return vertices

def rotar(vertices,listaR):

    if len(listaR) > 1:
        for i in range(len(listaR)):
            if i >= len(listaR) - 1:
                break
            else:
                if (listaR[i][1][0] == listaR[i + 1][1][0]) and (listaR[i][1][1] == listaR[i + 1][1][1]):
                    listaR[i][0] += listaR[i + 1][0]
                    listaR.pop(i + 1)

    for i in range(len(listaR)):
        xpiv = listaR[i][1][0]
        ypiv = listaR[i][1][1]

        angulo = listaR[i][0]

        rad = (angulo * math.pi) / 180
        for e in range(len(vertices)):

            vx = vertices[e][0]
            vy = vertices[e][1]

            vertices[e][0] = xpiv + (vx - xpiv) * math.cos(rad) - (vy - ypiv) * math.sin(rad)
            vertices[e][1] = ypiv + (vx - xpiv) * math.sin(rad) + (vy - ypiv) * math.cos(rad)

    return vertices

def escalar_con_pp(vertices, listaep):
    if len(listaep) > 1:
        for i in range(len(listaep)):
            if i >= len(listaep) - 1:
                break
            else:
                if (listaep[i][1][0] == listaep[i + 1][1][0]) and (listaep[i][1][1] == listaep[i + 1][1][1]):
                    listaep[i][0][0] *= listaep[i + 1][0][0]
                    listaep[i][0][1] *= listaep[i + 1][0][1]
                    listaep.pop(i + 1)
    for i in range(len(listaep)):
        xpiv = listaep[i][1][0]
        ypiv = listaep[i][1][1]
        xpive = listaep[i][0][0]
        ypive = listaep[i][0][1]

        for e in range(len(vertices)):
            vx = vertices[e][0]
            vy = vertices[e][1]
            vertices[e][0] = xpiv + xpive * (vx - xpiv)
            vertices[e][1] = ypiv + ypive * (vy - ypiv)
    return vertices

#BUSCA LA DISTANCIA ENTRE LOS VERTICES PARA DETERMINAR LA DISTANCIA MAS CORTA 
def distancia(lista,listaaux):
 
    listaaux2=[0,0]
    distanciamenor=0
    for i in range(len(lista)):

        x2=listaaux[0]
        y2=listaaux[1]

        x1=lista[i][0]
        y1=lista[i][1]

        r=((x2-x1)**2)
        h=((y2-y1)**2)
        distancia= math.sqrt((r+h))
        if i == 0 :
            distanciamenor=distancia
            listaaux2[0]=x1
            listaaux2[1]=y1
        if distancia<distanciamenor:
            distanciamenor= distancia
            listaaux2[0]=x1
            listaaux2[1]=y1
    lista.remove(listaaux2)
    return lista,listaaux2

#ACOMODA LOS VERTICES EN UN ORDEN PARA SER GRAFICADOS 
def acomodarLista(lista):
    listaF=[]
    listaaux=[0,0]
    xmin=lista[0][0]

    for i in range(len(lista)):
        x=lista[i][0]
        y=lista[i][1]
        if x<=xmin:
            xmin=x
            listaaux[0]=x
            listaaux[1]=y

    listaF.append(listaaux)
    lista.remove(listaaux)

    while len(lista)>0:
        lista,listaaux=distancia(lista,listaaux)
        listaF.append(listaaux)

    return listaF

def imprimirVertice(vertices):
    for i in range(len(vertices)):
        print("(",vertices[i][0],",",vertices[i][1],")")

a=True
while a:
    nVertice= int(input("¿Cuántos vertices tiene su figura?: "))
    if nVertice<3:
        print("Necesitas introducir más de dos vértices")
    else:
        a=False
        
vertices=[]
traslacion=[]
rotacion=[]
escalamiento=[]
escalamientopp = []

for i in range(nVertice):
    aux = []
    print('Vértice ', i+1)
    x= int(input("Ingrese su coordenada X del vértice: "))
    x=float(x)
    aux.append(x)
    y= int(input("Ingrese su coordenada Y del vértice: "))
    y=float(y)
    aux.append(y)
    vertices.append(aux)

print()
print("---------Menú de opciones--------" )
print("Opción 1: Traslación " )
print("Opción 2: Rotación " )
print("Opción 3: Escalamiento " )
print("Opción 4: Escalamiento con punto pivote")
print("Opción 5: Ejecutar " )
print()


selec= True
while selec:
    r=int(input("¿Qué operación desea realizar?: "))
    aux=[]

    if r== 1:
        x= int(input("Ingrese el aumento en X: "))
        aux.append(x)
        y= int(input("Ingrese el aumento en Y: "))
        aux.append(y)
        traslacion.append(aux)
        print()
    elif r== 2:
        aux2=[]
        z=input("Ingrese el ángulo de rotación: ")
        z=float(z)
        x= int(input("Ingrese la coordenada X del punto pivote: "))
        x=float(x)
        aux2.append(x)
        y= int(input("Ingrese la coordenada Y del punto pivote: "))
        y=float(y)
        aux2.append(y)

        aux.append(z)
        aux.append(aux2)
        rotacion.append(aux)

        print()
    elif r== 3:
        auxesc=[]
        z= input("Ingrese el índice de escalamiento en X: ")
        z=float(z)
        r= input("Ingrese el índice de escalamiento en Y: ")
        r=float(r)
        auxesc.append(z)
        auxesc.append(r)
        escalamiento.append(auxesc)
        print()
    elif r == 4:
        auxescc = []
        auxescc2 = []
        z = input("Ingrese el índice de escalamiento en X: ")
        z = float(z)
        auxescc.append(z)
        r = input("Ingrese el índice de escalamiento en Y: ")
        r = float(r)
        auxescc.append(r)
        x = input("Coordenada X del punto pivote: ")
        x = float(x)
        auxescc2.append(x)
        y = input("Coordenada Y del punto pivote: ")
        y = float(y)
        auxescc2.append(y)
        aux.append(auxescc)
        aux.append(auxescc2)
        escalamientopp.append(aux)
        print()

    elif r==5.:
        selec = False
        print("Selecciones terminadas")
        print()
    else:
        print("Opción no válida")


print("Acomodar vértices inicial: ")
vertices=acomodarLista(vertices)
imprimirVertice(vertices)


fig,ax = plt.subplots()
#Acomoda la grafica
plt.subplots_adjust(right=0.7)

print()

X,Y=acomodarVertices(vertices)
#Por si no exsiste
auxX = []
auxY = []
p, = ax.plot(X,Y,'g')


if len(rotacion)>0:
    print("Vértices antes de rotar:")
    imprimirVertice(vertices)
    print()
    print("Vértices rotados:")
    vertices=rotar(vertices,rotacion)
    imprimirVertice(vertices)

    X,Y=acomodarVertices(vertices)
    p1, = ax.plot(X,Y,'r')

if "p1" in globals() :
    True
else:
    p1, = ax.plot(auxX, auxX, color="r")

    

print()

if len(traslacion)>0:
    print("Vértices antes de trasladarse:")
    imprimirVertice(vertices)
    print()
    print("Vértices trasladados:")
    vertices=trasladar(vertices, traslacion)
    imprimirVertice(vertices)

    X,Y=acomodarVertices(vertices)
    p2, = ax.plot(X, Y,'y')
#Por si no exsiste p2
if "p2" in globals() :
    True
else:
    p2, = ax.plot(auxX, auxX, color="y")


print()

if len(escalamiento)>0:
    print("Vértices antes de escalarse:")
    imprimirVertice(vertices)
    print()
    print("Vértices escalados:")
    vertices=escalar(vertices,escalamiento)
    imprimirVertice(vertices)

    X,Y=acomodarVertices(vertices)
    p3, = ax.plot(X, Y,'c')
#Por si no exsiste p3
if "p3" in globals() :
    True
else:
    p3, = ax.plot(auxX, auxX, color="c")

print() 

if len(escalamientopp) > 0:
    print("Vértices antes del escalamiento con pivote:")
    imprimirVertice(vertices)
    print()
    print("Vértices escalados con punto pivote:")
    vertices = escalar_con_pp(vertices, escalamientopp)
    imprimirVertice(vertices)

    X,Y = acomodarVertices(vertices)
    p4, = ax.plot(X, Y, 'k')
#Por si no exsiste p4
if "p4" in globals() :
    True
else:
    p4, = ax.plot(auxX, auxX, color="k")
print()

print("Vértices finales acomodados")
vertices=acomodarLista(vertices)
imprimirVertice(vertices)

X,Y=acomodarVertices(vertices)
p5, = ax.plot(X, Y, 'm')

#Insetamos las coordenadas
lines = [p, p1, p2, p3, p4, p5]
labels = ["Original", "Rotación", "Traslación", "Escalamiento", "Escalamiento PP", "Final"]

def func(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    fig.canvas.draw()
 
 
label = [True, True, True, True, True, True]
 
# [Posicion izquierda, posicion derecha, ancho, alto]
ax_check = plt.axes([0.75, 0.001, 0.23, 0.3])
plot_button = CheckButtons(ax_check, labels, label)
plot_button.on_clicked(func)
 
plt.show()