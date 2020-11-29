### Información del repositorio
En este repositorio encontramos la entrega de la práctica 3 de la asignatura SCAV (parte de vídeo).

Tenemos 5 archivos .py y en cada de uno de ellos encontramos una explicación detallada sobre cómo utilizarlos:

##  **ex1.py**
En este script introducimos el nombre del vídeo "Big Buck Bunny", recortamos el primer minuto y generamos los siguientes archivos:
- Un archivo mp3 con el audio en formato mono.
- Un archivo mp3 con el audio con un bit rate de 24kb.
- Un archivo mp4 con el video de 1 minuto además de los subtítulos.

Una vez hemos generado todos estos archivos, creamos un container donde los combinamos.
A continuación vemos el contenido resultante:

<img src="https://drive.google.com/uc?export=view&id=1zFBKjD37DKAEZkDnguHInbi9Qq6zKxLn" width="300">


##  **ex2.py**
Gracias a este script, podemos generar un container personalizado de manera automática. Cuando lo ejecutamos introducimos el número de archivos que introduciremos en el container y para cada uno de ellos insertamos el nombre y el número de canales que tiene.

Cuando terminamos de insertar la inromación generamos el container.

En la siguiente imagen vemos el resultado de generar un container con los dos archivos de audio del apartado anterior:

<img src="https://drive.google.com/uc?export=view&id=1-_GNXOlCRv5MD8Fj4tL7b_Na4bK87LqD" width="300">


##  **ex3.py**
En este script introducimos el nombre de un container y obtenemos cuáles de los formatos de broadcast serían compatibles (DVB, ISDB, ATSC, DTMB) para enviarlo o un mensaje de error en caso de que no haya ninguno.

El resultado que obtenemos para el container del primer apartado es el siguiente:

<img src="https://drive.google.com/uc?export=view&id=1UUExRy7kMKfZESqQuFIhQl0_Ktak8sGm" width="300">


##  **ex4.py**
En este script simplemente llamamos al script 2 y consicutivamente al 3, de manera que generamos un container personalizado y miramos con qué formatos de broadcast es compatible.


##  **ex5.py**
Finalmente tenemos un script en el que además de crear una clase donde cada  una de las funciones disponibles nos permiten ejecutar los scripts anteriores. Además también encontramos un menú desde el cual podemos acceder a cualquiera de ellos. 

<img src="https://drive.google.com/uc?export=view&id=15NLUzS6RGqkMxtHm0hzqKLw6MS3uotnQ" width="300">
