
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, CheckButtons 
import operaciones as op

import gc


class transformacion:

    def __init__(self):
        self.nVertice=0
        self.vertices=[]
        self.lisTraslacion=[]
        self.lisRotacion=[]
        self.lisEscalamiento=[]
        self.lisEscalamientopp = []


    def operar(self):

        print("Acomodar vértices inicial: ")
        self.vertices=op.acomodarLista(self.vertices)
        op.imprimirVertice(self.vertices)


        X,Y=op.acomodarVertices(self.vertices)
        ar=plt.subplot(2,3,1)
        ar.plot(X,Y)
        ar.set_title("Figura Original", fontsize=12)


        ar=plt.subplot(2,3,2)
        ar.set_title("Rotación", fontsize=12)
        if len(self.lisRotacion)>0:
            print("Vértices antes de rotar:")
            op.imprimirVertice(self.vertices)
            print()
            print("Vertices rotados:")
            self.vertices=op.rotar(self.vertices,self.lisRotacion)
            op.imprimirVertice(self.vertices)

            X,Y=op.acomodarVertices(self.vertices)
            ar.plot(X,Y, color="r")

        print()
        ar=plt.subplot(2,3,3)
        ar.set_title("Traslacion", fontsize=12)
        if len(self.lisTraslacion)>0:
            print("Vértices antes de trasladarse:")
            op.imprimirVertice(self.vertices)
            print()
            print("Vértices trasladados:")
            self.vertices=op.trasladar(self.vertices, self.lisTraslacion)
            op.imprimirVertice(self.vertices)

            X,Y=op.acomodarVertices(self.vertices)
            ar.plot(X,Y, color="g")

        print()

        ar=plt.subplot(2,3,4)
        ar.set_title("Escalamiento", fontsize=12)
        if len(self.lisEscalamiento)>0:
            print("Vértices antes de escalarse:")
            op.imprimirVertice(self.vertices)
            print()
            print("Vértices escalados:")
            self.vertices=op.escalar(self.vertices,self.lisEscalamiento)
            op.imprimirVertice(self.vertices)

            X,Y=op.acomodarVertices(self.vertices)
            ar.plot(X,Y, color="magenta")
        print() 


        ar=plt.subplot(2,3,5)
        ar.set_title("Escalamiento PP", fontsize=12)
        if len(self.lisEscalamientopp) > 0:
            print("Vértices antes del escalamiento con pivote:")
            op.imprimirVertice(self.vertices)
            print()
            print("Vértices escalados con punto pivote:")
            self.vertices = op.escalar_con_pp(self.vertices, self.lisEscalamientopp)
            op.imprimirVertice(self.vertices)
            X,Y = op.acomodarVertices(self.vertices)
            ar=plt.subplot(2,3,5)
            ar.plot(X,Y,"black")

        print()

        print("Vertices finales acomodados")
        self.vertices=op.acomodarLista(self.vertices)
        op.imprimirVertice(self.vertices)

        X,Y=op.acomodarVertices(self.vertices)
        ar=plt.subplot(2,3,6)
        ar.plot(X,Y,"y")
        ar.set_title("Figura Final", fontsize=12)
        plt.show()



if __name__ == "__main__":

    T1 = transformacion()

    a=True
    while a:
        T1.nVertice= int(input("¿Cuántos vertices tiene su figura?: "))
        if T1.nVertice<3:
            print("Necesitas introducir más de dos vértices")
        else:
            a=False
            
    for i in range(T1.nVertice):
        aux = []
        print('Vértice ', i+1)
        x= int(input("Ingrese su coordenada X del vértice: "))
        x=float(x)
        aux.append(x)
        y= int(input("Ingrese su coordenada Y del vértice: "))
        y=float(y)
        aux.append(y)
        T1.vertices.append(aux)
    
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
            T1.lisTraslacion.append(aux)
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
            T1.lisRotacion.append(aux)

            print()
        elif r== 3:
            auxesc=[]
            z= input("Ingrese el índice de lisEscalamiento en X: ")
            z=float(z)
            r= input("Ingrese el índice de lisEscalamiento en Y: ")
            r=float(r)
            auxesc.append(z)
            auxesc.append(r)
            T1.lisEscalamiento.append(auxesc)
            print()
        elif r == 4:
            auxescc = []
            auxescc2 = []
            z = input("Ingrese el índice de lisEscalamiento en X: ")
            z = float(z)
            auxescc.append(z)
            r = input("Ingrese el índice de lisEscalamiento en Y: ")
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
            T1.lisEscalamientopp.append(aux)
            print()

        elif r==5.:
            selec = False
            print("Selecciones terminadas")
            print()
        else:
            print("Opción no válida")

    T1.operar()