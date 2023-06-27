
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

def trasladar3D(vertices, listaT):
    aumX=0
    aumY=0
    aumZ=0

    for i in range(len(listaT)):
        aumX+=listaT[i][0]
        aumY+=listaT[i][1]
        aumZ+=listaT[i][2]

    for i in range(len(vertices)):
        vertices[i][0]= vertices[i][0] + aumX
        vertices[i][1]= vertices[i][1] + aumY
        vertices[i][2]= vertices[i][2] + aumZ

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

def escalar3D(vertices, listaE):
    escalaX=1
    escalaY=1
    escalaZ=1

    for i in range(len(listaE)):
        escalaX*=listaE[i][0]
        escalaY*=listaE[i][1]
        escalaZ*=listaE[i][2]

    for i in range(len(vertices)):
        vertices[i][0]= vertices[i][0] * escalaX
        vertices[i][1]= vertices[i][1] * escalaY
        vertices[i][2]= vertices[i][2] * escalaZ
    
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


def rotar3D(vertices,listaR):
    if len(listaR) > 1:
        for i in range(len(listaR)):
            if i >= len(listaR) - 1:
                break
            else:
                if (listaR[i][1][0] == listaR[i + 1][1][0]) and (listaR[i][1][1] == listaR[i + 1][1][1]):
                    listaR[i][0] += listaR[i + 1][0]
                    listaR.pop(i + 1)

    for i in range(len(listaR)):
        xpiv = listaR[i][2][0]
        ypiv = listaR[i][2][1]
        zpiv = listaR[i][2][2]


        angulo = listaR[i][0]

        rad = (angulo * math.pi) / 180
        for e in range(len(vertices)):

            vx = vertices[e][0]
            vy = vertices[e][1]
            vz = vertices[e][2]

            if listaR[i][1] == "xy":
                vertices[e][0] = xpiv + (vx - xpiv) * math.cos(rad) - (vy - ypiv) * math.sin(rad)
                vertices[e][1] = ypiv + (vx - xpiv) * math.sin(rad) + (vy - ypiv) * math.cos(rad)

            elif listaR[i][1] == "yz":
                vertices[e][1] = ypiv + (vy - ypiv) * math.cos(rad) - (vz - zpiv) * math.sin(rad)
                vertices[e][2] = zpiv + (vy - ypiv) * math.sin(rad) + (vz - zpiv) * math.cos(rad)
            
            elif listaR[i][1] == "xz":
                vertices[e][0] = xpiv + (vx- xpiv) * math.cos(rad) - (vz - zpiv) * math.sin(rad)
                vertices[e][2] = zpiv + (vx - xpiv) * math.sin(rad) + (vz - zpiv) * math.cos(rad)

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

def escalar_con_pp3D(vertices, listaep):

    if len(listaep) > 1:
        for i in range(len(listaep)):
            if i >= len(listaep) - 1:
                break
            else:
                if (listaep[i][1][0] == listaep[i + 1][1][0]) and (listaep[i][1][1] == listaep[i + 1][1][1]) and (listaep[i][1][2] == listaep[i + 1][1][2]):
                    listaep[i][0][0] *= listaep[i + 1][0][0]
                    listaep[i][0][1] *= listaep[i + 1][0][1]
                    listaep[i][0][2] *= listaep[i + 1][0][2]
                    listaep.pop(i + 1)

    for i in range(len(listaep)):
        xpiv = listaep[i][1][0]
        ypiv = listaep[i][1][1]
        zpiv = listaep[i][1][2]
        xpive = listaep[i][0][0]
        ypive = listaep[i][0][1]
        zpive = listaep[i][0][2]

        for e in range(len(vertices)):
            vx = vertices[e][0]
            vy = vertices[e][1]
            vz = vertices[e][2]

            vertices[e][0] = xpiv + xpive * (vx - xpiv)
            vertices[e][1] = ypiv + ypive * (vy - ypiv)
            vertices[e][2] = zpiv + zpive * (vz - zpiv)
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

def ordenarVertices3D(nVertices, vertices):
    X=[]
    Y=[]
    Z=[]

    if nVertices == 5:
        for i in range(4):
            X.append(vertices[i][0])
            Y.append(vertices[i][1])
            Z.append(vertices[i][2])

        X.append(vertices[0][0])
        Y.append(vertices[0][1])
        Z.append(vertices[0][2])

        for i in range(4):
            X.append(vertices[-1][0])
            Y.append(vertices[-1][1])
            Z.append(vertices[-1][2])

            X.append(vertices[i][0])
            Y.append(vertices[i][1])
            Z.append(vertices[i][2])

        return X,Y,Z
    else:
        for i in range(4):
            X.append(vertices[i][0])
            Y.append(vertices[i][1])
            Z.append(vertices[i][2])

        X.append(vertices[0][0])
        Y.append(vertices[0][1])
        Z.append(vertices[0][2])

        for i in range(4):
            X.append(vertices[-4+i][0])
            Y.append(vertices[-4+i][1])
            Z.append(vertices[-4+i][2])

        X.append(vertices[4][0])
        Y.append(vertices[4][1])
        Z.append(vertices[4][2])

        X.append(vertices[5][0])
        Y.append(vertices[5][1])
        Z.append(vertices[5][2])

        X.append(vertices[1][0])
        Y.append(vertices[1][1])
        Z.append(vertices[1][2])

        X.append(vertices[2][0])
        Y.append(vertices[2][1])
        Z.append(vertices[2][2])

        X.append(vertices[6][0])
        Y.append(vertices[6][1])
        Z.append(vertices[6][2])

        X.append(vertices[7][0])
        Y.append(vertices[7][1])
        Z.append(vertices[7][2])

        X.append(vertices[3][0])
        Y.append(vertices[3][1])
        Z.append(vertices[3][2])

        return X,Y,Z


def imprimirVertice(vertices):
    for i in range(len(vertices)):
        print("(",vertices[i][0],",",vertices[i][1],")")

def imprimirVertice3D(vertices):
    for i in range(len(vertices)):
        print("(",vertices[i][0],",",vertices[i][1],", ",vertices[i][2],")")