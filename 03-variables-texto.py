"""
Otro de los tipos de datos que podemos trabajar con variables son los textos, 
la manera de crear la variable es muy similar a con los números, pero para 
que Python reconozca que nuestra variable es de tipo texto debemos "encerrar" 
el texto usando comillas, simples (') o dobles ("). Este es un mundo muy 
grande como para explicarlo solo en un archivo, pero te mostraré algunos 
aspectos utiles de cómo trabajar con textos.

Creemos una variable que almacene un mensaje, también imprimamos por pantalla 
su valor y su tipo
"""
message = "Hola Mundo"
print(message)
print(type(message))

"""
Este tipo de datos se les llama "str" (mas conocido como String, que 
significa cadena de texto), hace referencia a textos, podemos usar distintas 
funciones y técnicas para manipularlo, notaste en el archivo anterior que 
los números podíamos sumarlos, te imaginas poder sumar textos? 

En estricto rigor esto no es posible, pero si podemos "concatenar" textos. 
Como viste anteriormente los textos son "cadenas de textos", esto significa 
que podemos usarlos como si fueran dos cadenas distintas, pero podemos 
unirlas usando la expresión "+" 

Ahora cambiaremos el valor de la variable "message" para que solo diga 
"Hola" y crearemos la variable "name" para almacenar nuestro nombre. Luego 
"concatenaremos" las cadenas "message" y "name" para imprimirlas en la 
consola.
"""
message = "Hola"
name = "Pepito"
regards = message + name
print(regards)

"""
Notarás que la impresión no se ve clara, dice "HolaPepito", falta un espacio, 
y lo que pasa es que las variables de texto tendrán tal cual el texto que le 
indiquemos, si queremos que entre medio quede un espacio debemos indicarle de
forma explícita ese espacio entonces a la variable "message" le agregaremos 
ese espacio y volveremos a imprimir el mismo saludo.

Nota: Descomenta el código a continuación para ver el resultado
"""
#message = "Hola " # <- acá agregamos el espacio al final
#name = "Pepito" # <- pero acá no lo hicimos, porque no lo necesitamos
#regards = message + name
#print(regards)

"""
Ya has visto que podemos concatenar texto con texto, pero también podemos 
hacerlo con numeros, pero acá hay un pequeño problema, 
Con los textos hay distintas funciones que nos son realmente útiles, veremos
algunas de ellas en el siguiente archivo.
"""
