
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


        fig,ax = plt.subplots()
        #Acomoda la grafica
        plt.subplots_adjust(right=0.7)

        print()

        X,Y=op.acomodarVertices(self.vertices)
        #Por si no exsiste
        auxX = []
        auxY = []
        p, = ax.plot(X,Y,'g')


        if len(self.lisRotacion)>0:
            print("Vértices antes de rotar:")
            op.imprimirVertice(self.vertices)
            print()
            print("Vértices rotados:")
            self.vertices=op.rotar(self.vertices,self.lisRotacion)
            op.imprimirVertice(self.vertices)

            X,Y=op.acomodarVertices(self.vertices)
            p1, = ax.plot(X,Y,'r')

        if "p1" in globals() :
            True
        else:
            p1, = ax.plot(auxX, auxX, color="r")

            

        print()

        if len(self.lisTraslacion)>0:
            print("Vértices antes de trasladarse:")
            op.imprimirVertice(self.vertices)
            print()
            print("Vértices trasladados:")
            self.vertices=op.trasladar(self.vertices, self.lisTraslacion)
            op.imprimirVertice(self.vertices)

            X,Y=op.acomodarVertices(self.vertices)
            p2, = ax.plot(X, Y,'y')
        #Por si no exsiste p2
        if "p2" in globals() :
            True
        else:
            p2, = ax.plot(auxX, auxX, color="y")


        print()

        if len(self.lisEscalamiento)>0:
            print("Vértices antes de escalarse:")
            op.imprimirVertice(self.vertices)
            print()
            print("Vértices escalados:")
            self.vertices=op.escalar(self.vertices,self.lisEscalamiento)
            op.imprimirVertice(self.vertices)

            X,Y=op.acomodarVertices(self.vertices)
            p3, = ax.plot(X, Y,'c')
        #Por si no exsiste p3
        if "p3" in globals() :
            True
        else:
            p3, = ax.plot(auxX, auxX, color="c")

        print() 

        if len(self.lisEscalamientopp) > 0:
            print("Vértices antes del lisEscalamiento con pivote:")
            op.imprimirVertice(self.vertices)
            print()
            print("Vértices escalados con punto pivote:")
            self.vertices = op.escalar_con_pp(self.vertices, self.lisEscalamientopp)
            op.imprimirVertice(self.vertices)

            X,Y = op.acomodarVertices(self.vertices)
            p4, = ax.plot(X, Y, 'k')
        #Por si no exsiste p4
        if "p4" in globals() :
            True
        else:
            p4, = ax.plot(auxX, auxX, color="k")
        print()

        print("Vértices finales acomodados")
        self.vertices=op.acomodarLista(self.vertices)
        op.imprimirVertice(self.vertices)

        X,Y=op.acomodarVertices(self.vertices)
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