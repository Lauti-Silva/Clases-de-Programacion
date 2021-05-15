def  positivo_negativo ( numero ):
    "" "determinar si el numero es positivo (devuelve true) o negativo (devuelve falso)" ""
    si ( numero > = 0 ):
        volver  verdadero
    otra cosa :
        volver  falso



def  contar_caracter ( cadena , caracter ):
    "" "contar cuantas veces aparece el caracter en la cadena" ""
    cantidad  =  0
    para  letra  en  cadena :
        si ( letra  ==  caracter ):
            cantidad  + =  1
    devolución  cantidad
    
def  es_palindromo ( cadena ):
    "" "determina si una cadena es palindromo" ""
    cadena_aux  =  lista ( cadena )
    cadena_aux . reverso ()
    cadena_invertida  =  ''
    cadena_invertida  =  cadena_invertida . unirse ( cadena_aux )

    return  cadena_invertida  ==  cadena

# def sumatoria (número):
# suma = 0
# para i en el rango (1, numero + 1):
# suma + = 1 / i
# return suma


def  cargar_datos ():
    "" "doctring de la funcion" ""
    nombre  =  input ( 'ingrese su nombre' )
    volver  nombre


def  suma ( numero1 , numero2 ):
    retorno  numero1  +  numero2

def  resta ( numero1 , numero2 ):
    return  numero1  -  numero2

def  producto ( numero1 , numero2 ):
    return  numero1  *  numero2

def  division ( numero1 , numero2 ):
    return  numero1  /  numero2


def  potencia ( base , exponente ):
    retorno  base  **  exponente

operaciones  = { '+' : suma , '-' : resta , '*' : producto , '/' : division , '^' : potencia }



def  calculadora ( numero1 , operador , numero2 ):
    if ( operador  en  operaciones ):
        return  operaciones [ operador ] ( numero1 , numero2 )
    otra cosa :
        regresar  Ninguno


def  es_vocal ( caracter ):
    vocales  = [ 'a' , 'e' , 'i' , 'o' , 'u' ]
    volver  caracter . inferior () en  vocales


def  sumatoria ( número ):
    total  =  0
    para  i  en el  rango ( 1 , numero + 1 ):
        total  + =  1 / i

    devolución  total

# imprimir (sumatoria (100))

# para i en el rango (1,10 + 1):
# imprimir (i)

# num1 = int (input ('ingrese un valor'))
# operador = input ('ingrese un operador')
# num2 = int (input ('ingrese un valor'))

# control = Verdadero

# while (control):
# num1 = calculadora (num1, operador, num2)
# print (num1)
# operador = input ('ingrese un operador')
# if (operador == '?'):
# control = Falso
# num2 = int (input ('ingrese un valor'))