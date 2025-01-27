"""
La impresión de información por consola suele ser una de las herramientas 
mas usadas a la hora del desarrollo, pero debe ser usada con cautela, porque 
en lugar de ayudarnos puede llevarnos a la confusión.

Para esto usaremos nuestra primera función, éstas se conforman por:
    - Nombre: Suele ser un nombre representativo de la acción que realiza.
    - Parámetros de entrada: Se ingresan entre los parentesis.
    - Dato de salida: Depende de cada función, dependiendo de cómo esté 
        programada. si devolverá un dato o no. Mas adelante lo veremos a 
        mayor detalle.

Siguiendo con el ejemplo anterior, usemos la función "print()" para imprimir 
por consola alguna cosa. Esta función pide que le ingresemos un objeto (en 
este caso usaremos la variable "shopping_cart" del código que está en el 
archivo 01-variables-numéricas.py - PARTE 1).

Nota: Puedes ejecutar tu primer programa presionando la tecla F5, talvez te 
pida que selecciones la opción "Start Debugging".
"""
apple = 6
avocado = 3
onion = 4
orange = 5

shopping_cart = apple + avocado + onion + orange

print(shopping_cart)
#print(type(shopping_cart)) # Esta linea mas adelante pediremos descomentarla

"""
Con esto podemos notar que la cantidad de productos que tenemos en nuestro 
"carritoDeCompras" es 18, Ahora intenta copiar el código de la PARTE 2, 
pegala a continuación y vuelve a imprimir su valor.
"""
#Tu código debería ir acá

"""
podrás notar que calculó la manzana y media que te comiste, pero te fijaste 
en que el formato del número cambió?. Lo que pasa es que los lenguajes de 
programación trabajan con distintos tipos de datos, hasta el momento solo 
hemos trabajado con datos numéricos, pero hay otros tipos de datos, 
descomenta la linea 26 borrando el "#" y vuelve a ejecutar el programa.
"""
"""
Ahora usaste otra función ("type()"), esta función recibe como parámetro de 
entrada un objeto (En este caso la variable "shopping_cart"), y retorna un 
texto, en este caso "<class 'int'>", ahora vuelve a escribir la linea 26 al 
final de tu programa. 
"""
#Tu código debería ir acá

"""
Efectivamente! el tipo de dato cambió, esto es posible porque Python es un 
lenguaje interpretado, esto quiere decir que el tipo de una variable se 
determina en tiempo de ejecución, por lo que no es necesario definirlo al 
crear la variable. Veamos cómo funcionan las variables de texto en el 
siguiente archivo.
"""