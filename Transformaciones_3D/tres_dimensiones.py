import operaciones as op
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, CheckButtons

def tresD(nvertices):
    vertices=[]
    traslacion3Dim=[]
    rotacion3D=[]
    escalamiento3D=[]
    escalamiento3DPP=[]

    print("El orden en el que ingrese los vertices será en el orden por el cual se unirán")
    print("En caso de 5 lados: Ingrese primero los datos de la base y luego la punta")
    print("En caso de 8 lados: Ingrese primero los datos de la base y luego los de la cara opuesta en el mismo orden")
    print()

    for i in range(nvertices):
        aux = []
        print('Vértice ', i+1)
        x= int(input("Ingrese su coordenada X del vértice: "))
        x=float(x)
        aux.append(x)
        y= int(input("Ingrese su coordenada Y del vértice: "))
        y=float(y)
        aux.append(y)
        z= int(input("Ingrese su coordenada Z del vértice: "))
        z=float(z)
        aux.append(z)
        vertices.append(aux)

    print()
    print("---------Menú de opciones--------" )
    print("Opción 1: Traslación 3D" )
    print("Opción 2: Rotación 3D" )
    print("Opción 3: Escalamiento 3D" )
    print("Opción 4: Escalamiento con punto pivote 3D" )
    print("Opción 5: Ejecutar " )
    print()

    selec= True
    while selec:
        r=int(input("¿Qué operación desea realizar?: "))
        aux=[]

        if r == 1:
            aux=[]
            x= int(input("Ingrese el aumento en X: "))
            x=float(x)
            aux.append(x)
            y= int(input("Ingrese el aumento en Y: "))
            y=float(y)
            aux.append(y)
            z= int(input("Ingrese el aumento en Z: "))
            z=float(z)
            aux.append(z)
            traslacion3Dim.append(aux)
            print()

        elif r== 2:
            aux=[]
            aux5=[]
            a=input("Ingrese el ángulo de rotación: ")
            a=float(a)
            x= int(input("Ingrese la coordenada X del punto pivote: "))
            x=float(x)
            aux5.append(x)
            y= int(input("Ingrese la coordenada Y del punto pivote: "))
            y=float(y)
            aux5.append(y)
            z= int(input("Ingrese la coordenada Z del punto pivote: "))
            z=float(z)
            aux5.append(z)
            e=input("Ingresa el eje de rotación (xy,yz,xz): ")
            aux.append(a)
            aux.append(e)
            aux.append(aux5)
            rotacion3D.append(aux)
            print()

        elif r== 3:
            auxesc=[]
            x= input("Ingrese el índice de escalamiento en X: ")
            x=float(x)
            y= input("Ingrese el índice de escalamiento en Y: ")
            y=float(y)
            z= input("Ingrese el índice de escalamiento en Z: ")
            z=float(z)
            auxesc.append(x)
            auxesc.append(y)
            auxesc.append(z)
            escalamiento3D.append(auxesc)
            print()

        elif r== 4:
            aux=[]
            auxesc=[]
            auxesc1=[]

            x= input("Ingrese el índice de escalamiento en X: ")
            x=float(x)
            y= input("Ingrese el índice de escalamiento en Y: ")
            y=float(y)
            z= input("Ingrese el índice de escalamiento en Z: ")
            z=float(z)
            auxesc.append(x)
            auxesc.append(y)
            auxesc.append(z)

            x1= input("Ingrese la coordenada del punto pivote en X: ")
            x1=float(x1)
            y1= input("Ingrese la coordenada del punto pivote en Y: ")
            y1=float(y1)
            z1= input("Ingrese la coordenada del punto pivote en Z: ")
            z1=float(z1)
            auxesc1.append(x1)
            auxesc1.append(y1)
            auxesc1.append(z1)

            aux.append(auxesc)
            aux.append(auxesc1)
            escalamiento3DPP.append(aux)
            print()
            
        elif r==5.:
            selec = False
            print("Selecciones terminadas")
            print()
        else:
            print("Opción no válida")



    fig = plt.figure(figsize=(8,5))
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_zlim(0, 10)
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_zlabel("Z")

    X,Y,Z=op.ordenarVertices3D(nvertices, vertices)
    ax1.plot(X, Y, Z, c='r', marker='o')


    if len(rotacion3D)>0:
        print("Vértices antes de rotar:")
        op.imprimirVertice3D(vertices)
        print("Vértices rotados:")
        vertices=op.rotar3D(vertices,rotacion3D)
        op.imprimirVertice3D(vertices)
        X,Y,Z=op.ordenarVertices3D(nvertices, vertices)
        ax1.plot(X, Y, Z, c='g', marker='o')


    if len(traslacion3Dim)>0:
        print("Vértices antes de trasladar:")
        op.imprimirVertice3D(vertices)
        print("Vértices trasladados:")
        vertices=op.trasladar3D(vertices,traslacion3Dim)
        op.imprimirVertice3D(vertices)
        X,Y,Z=op.ordenarVertices3D(nvertices, vertices)
        ax1.plot(X, Y, Z, c='y', marker='o')
    
    if len(escalamiento3D)>0:
        print("Vértices antes de escalar:")
        op.imprimirVertice3D(vertices)
        print("Vértices escalados:")
        vertices=op.escalar3D(vertices,escalamiento3D)
        op.imprimirVertice3D(vertices)
        X,Y,Z=op.ordenarVertices3D(nvertices, vertices)
        ax1.plot(X, Y, Z, c='m', marker='o')
    
    if len(escalamiento3DPP)>0:
        print("Vértices antes de escalar:")
        op.imprimirVertice3D(vertices)
        print("Vértices escalados:")
        vertices=op.escalar_con_pp3D(vertices,escalamiento3DPP)
        op.imprimirVertice3D(vertices)
        X,Y,Z=op.ordenarVertices3D(nvertices, vertices)
        ax1.plot(X, Y, Z, c='c', marker='o')
    else:
        print("Fin del proceso")

    plt.show()