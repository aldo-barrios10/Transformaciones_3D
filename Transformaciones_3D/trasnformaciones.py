import operaciones as op
import tres_dimensiones as d3
import dos_dimensiones as d2

if __name__ == "__main__":

    a=True
    while a:
        
        nDimensiones=int(input("¿Cuántas dimensiones tiene su figura?: "))

        if nDimensiones == 3:

            nVertice= int(input("¿Cuántos vértices tiene su figura? (5 u 8 Vertices): "))
            if nVertice==5 or nVertice == 8:      
                a=False
            else:
                print("Necesitas introducir un número válido de vértices")

            
        elif nDimensiones == 2:

            nVertice= int(input("¿Cuántos vértices tiene su figura?: "))
            if nVertice<3:
                print("Necesitas introducir más de dos vértices")
            else:
                a=False
        
        else: 
            print("Número no válido")


    if nDimensiones == 3:
        d3.tresD(nVertice)
    else:
        d2.dosD(nVertice)