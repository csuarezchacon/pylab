"""
Las variables son la unidad base de almacenamiento en la programación y como 
su nombre lo indica, el valor de una variable ... puede variar (daah).

Separaremos este ejemplo en dos partes:

PARTE 1

Para entender cómo funcionan las variables imaginemos que vamos de compras a 
la feria, comunmente cada producto lo guardamos en una bolsa diferente, así 
es como terminamos con distintas bolasa con manzanas, naranjas, paltas, etc. 
Entonces le diremos a python que tenemos distintas bolsas para cada producto  
tal como lo haríamos con una compra habitual  también le diremos cuantas 
unidades hay en cada bolsa. (a modo de evitar la redundancia omitiremos la 
palabra "bolsa" y usaremos los nombres de variables en ingles, esta es una 
buena práctica)

Ten en cuenta que las variables constan de dos propiedades, nombre y valor.

Entonces crearemos las distintas variables que representan las distintas 
bolsas de productos.
"""
apple = 6
avocado = 3
onion = 4
orange = 5

"""
Python ahora sabe que hemos creado 4 variables que tienen distintos valores, 
podrás notar que todos ellos son números, y Python nos permite realizar 
operaciones matemáticas con ellos, sumemos los distintos productos que hemos 
comprado y almacenemoslo en la variable "shopping_cart". 
"""
shopping_cart = apple + avocado + onion + orange

"""
PARTE 2

Imagina además que en el camino a la casa te dió hambre, y te comiste ...
una manzana y media :O, Para este ejemplo actualizaremos el valor de la 
variable "apple" y volveremos a hacer el cálculo del "shopping_cart"
"""
apple = apple - 1.5
shopping_cart = apple + avocado + onion + orange

"""
Te imaginas qué valor tiene ahora el "shopping_cart"?, veamos cómo podemos 
ver el reaultado de nuestro código en acción en el siguiente archivo.
"""