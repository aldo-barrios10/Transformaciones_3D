# Transformaciones Geométricas
<div align="justify" >
Este repositorio cuenta con 3 versiones de algoritmos de transformaciones geométricas, las cuales son, roatación, traslación y escalamiento.
A su vez, los 3 scripts cuentan con la posibilidad de graficar estas transformaciones que, de manera sencilla, permiten ver las diferencias de las figuras y cómo se comportan con cada una e las transformaciones.
</div>

## Especificaciones
<div align="justify" >
Los algoritmos están diseñados con Python 3.10, por lo que, para evitar problemas, deberá de ejecutarse en esta versión o superior. Por otra parte, para las graficas se utilizó la libreria matplotlib, por lo que será necesaria su instalación para que se piueda correr el código.
</div>

## índice
- Transformaciones_3D: Transformaciones y gráfica 3D.
- Transformaciones_Grafica_Individual: Transformaciones 2D con gráfica para cada transformación.
- Transformaciones_Grafica_unica: Transformaciones 2D con una sola gáfica para comparación.
- Codigos_unico_script: Un solo archivo para cada algoritmo.

## Uso y ejemplos
<div align="justify" >
Los códigos son diferentes entre sí, pero cuentan con caracteristicas muy similares, siendo la forma de graficar la diferencia más notable entre todos.,
A continuación se dará una explicación de cómo usar cada uno de los códigos.
</div>

### Input
La entrada de los algortimos 2D es bastante sencilla, en esta se tendrá que especificar el numero de vertices de la figura y posteriormente dar las coordenadas de estos mismos.

<div align="center" >
  
![](https://github.com/aldo-barrios10/Transformaciones_3D/blob/main/recursos/input_1.png)
</div>

<div align="justify" >
En el caso del algoritmo 3D se deberá especificar si la figura tiene 5 u 8 vertices, posteriormente se deberán agregar los puntos de una manera especifica, ya que para poder graficar la figura se usará este mismo orden, de no hacerse de esta manera, el algoritmo hará las operaciones sin problema, sin embargo, al graficar la figura se verá unida de manera incorrecta.
</div>
<br>
<div align="center" >
  
![](https://github.com/aldo-barrios10/Transformaciones_3D/blob/main/recursos/input_3.png)
</div>
Una vez introducidos los datos, se deberán elegir las transformaciones que se desean relaizar, teniendo un menú en donde aparecen todas la sposibilidades y en donde se deberá introducir el número de la operación, posteriormente se pedirán los datos acorde a cada uno de las operaciones. En el algoritmo 3D se pedirá un dato extra, el cual será la posición en Z, además de que si se usa la opción de rotra, se deberá introduir el eje en el que se desee rotar, tenideno como opciones validas el eje xy, xz y yz.

<div align="center" >
  
![](https://github.com/aldo-barrios10/Transformaciones_3D/blob/main/recursos/input_2.png)
</div>
Una vez terminadas las selecciones, se debe de precionar la opción 5 para poder ejecutar el algoritmo y asi ver las gráficas resultantes de las transformaciones.

### Output
<div align="justify" >
Una vez dada la opción 5, el algoritmo realizará un acomodo de vertices para asegurarse de que se realice el proceso de manera correcto, posteriormente realizará las operaciones en el siguiente orden: rotación, traslación, escalamiento y escalamiento con punto pivote.
Al terminar de realizar las operaciones, los 3 algoritmos nos arroján los resultados de esta manera, en donde veremos las coordenadas de cada uno de los puntos en la terminal y en qué orden fueron realizadas, permitiendo dar seguimiento a ca da una de las transformaciones de manera más detallada.
</div>

<br>
<div align="center" >
  
![](https://github.com/aldo-barrios10/Transformaciones_3D/blob/main/recursos/output.png)
</div>

A su vez, dependiendo del código este arrojará una gráfica en la que se podran ver cada una de las figuras transformadas. La gráficas que se muestarn son las siguinetes:
- Transformaciones_3D.py:
  <br>
  <br>
  <div align="center" >
  <img aling="center" width="550" height="400" src="https://github.com/aldo-barrios10/Transformaciones_3D/blob/main/recursos/tf_g3.png" />
  </div>
  <br>
  <br>
- Transformaciones_Grafica_Individual.py:
  <br>
  <br>
  <div align="center" >
  <img aling="center" width="550" height="400" src="https://github.com/aldo-barrios10/Transformaciones_3D/blob/main/recursos/tf_g2.png" />
  </div>
  <br>
  <br>
- Transformaciones_Grafica_unica.py:
  <br>
  <br>
  <div align="center" >
  <img aling="center" width="550" height="400" src="https://github.com/aldo-barrios10/Transformaciones_3D/blob/main/recursos/tf_g1.png" />
  </div>
