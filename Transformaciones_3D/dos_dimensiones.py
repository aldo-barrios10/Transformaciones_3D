import operaciones as op
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, CheckButtons

def dosD(nvertices):
    vertices=[]
    traslacion=[]
    rotacion=[]
    escalamiento=[]
    escalamientopp = []

    for i in range(nvertices):
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
            aux=[]
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
    vertices=op.acomodarLista(vertices)
    op.imprimirVertice(vertices)


    fig,ax = plt.subplots()
    #Acomoda la grafica
    plt.subplots_adjust(right=0.7)

    print()

    X,Y=op.acomodarVertices(vertices)
    #Por si no exsiste
    auxX = []
    auxY = []
    p, = ax.plot(X,Y,'g')


    if len(rotacion)>0:
        print("Vértices antes de rotar:")
        op.imprimirVertice(vertices)
        print()
        print("Vértices rotados:")
        vertices=op.rotar(vertices,rotacion)
        op.imprimirVertice(vertices)

        X,Y=op.acomodarVertices(vertices)
        p1, = ax.plot(X,Y,'r')

    if "p1" in globals() :
        True
    else:
        p1, = ax.plot(auxX, auxX, color="r")

        

    print()

    if len(traslacion)>0:
        print("Vértices antes de trasladarse:")
        op.imprimirVertice(vertices)
        print()
        print("Vértices trasladados:")
        vertices=op.trasladar(vertices, traslacion)
        op.imprimirVertice(vertices)

        X,Y=op.acomodarVertices(vertices)
        p2, = ax.plot(X, Y,'y')
    #Por si no exsiste p2
    if "p2" in globals() :
        True
    else:
        p2, = ax.plot(auxX, auxX, color="y")


    print()

    if len(escalamiento)>0:
        print("Vértices antes de escalarse:")
        op.imprimirVertice(vertices)
        print()
        print("Vértices escalados:")
        vertices=op.escalar(vertices,escalamiento)
        op.imprimirVertice(vertices)

        X,Y=op.acomodarVertices(vertices)
        p3, = ax.plot(X, Y,'c')
    #Por si no exsiste p3
    if "p3" in globals() :
        True
    else:
        p3, = ax.plot(auxX, auxX, color="c")

    print() 

    if len(escalamientopp) > 0:
        print("Vértices antes del escalamiento con pivote:")
        op.imprimirVertice(vertices)
        print()
        print("Vértices escalados con punto pivote:")
        vertices = op.escalar_con_pp(vertices, escalamientopp)
        op.imprimirVertice(vertices)

        X,Y = op.acomodarVertices(vertices)
        p4, = ax.plot(X, Y, 'k')
    #Por si no exsiste p4
    if "p4" in globals() :
        True
    else:
        p4, = ax.plot(auxX, auxX, color="k")
    print()

    print("Vértices finales acomodados")
    vertices=op.acomodarLista(vertices)
    op.imprimirVertice(vertices)

    X,Y=op.acomodarVertices(vertices)
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