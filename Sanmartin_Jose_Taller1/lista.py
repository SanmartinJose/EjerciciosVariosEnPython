import os, big_o,re
def PrimerNoRepetido(cadena):
    """
     Es una funcion la cual toma una cadena de numeros y realiza un conteo para analizar cuantos 
     elementos se encuentran repetidos, y devolver solo el primero que se encuentre repetido 
    Recibe:
    ------------
      cadena:Es la cadena de caracteres que se va a recibir 
           
    Retorna:
    ------------
       no retorna ningun parametro
    """
    #se crea un diccionario que va a guardar el numero de coincidencias en el parametro cadena 
    conteo={}
    #Pasa por cada unos de los caracteres de la variable cadena 
    for caracter in cadena:
    #Si el caracarter se encuentra dentro de la variable conteo
        if caracter in conteo:
            #Entonces se tendra que vamos a aumetar en uno al diccionnario
            conteo[caracter] += 1
            #Caso contrario si no se encuentra en el diccionario el caracter
        else:
            #iniciamos desde 1
            conteo[caracter] = 1
    #se realiza una itereacion por cada una de las llaves que integran conteo       
    for caracter in conteo.keys():
        #si dentro de estas llaves se encuentra solo uno de los caracteres 
        if conteo[caracter]!=1:
            #nos retorna ese caracter 
            return caracter
       
        
    
        
def solution(numeros):
    """
     Es una funcion en la cual vamos a verificar los datos para posteriormente imprimir un resultado
     adecuado para este 
     Recibe 
    ------------
     numero: Recibe un cadena de numeros que se va repasar
           
    Retorna:
    ------------
       Retrona el numero que no se repite 
       """
    #Creamos un buclue while en el que se repite una accion hasta que las condiciones sean correctas 
   
    #Convertimos en una lista String a los caracteres Numericos 
    lista=(list(str(numeros)))
    #retorna el primer numero no repetido de la lista 
    return PrimerNoRepetido(lista)
   
        

if __name__ == '__main__':
  while(True):
        #Se crea un try para comprobar las condiciones 
        try:
        #Se pide que ingresamos una cadena de numeros 
            cadena=(input("Ingrese la cadena de números: "))
        #Se crea la expecion a la regla 
        except ValueError:
            #Se crea un mensaje de advertencia
            print("No valido intente de nuevo(Deben ser solo numeros)")
            #Si las condiciones son adecuadas se continua 
            continue
        #Se sale del bucle While 
        break

   
    #Imprime el resultado
patron=solution(cadena)
    #Creamos la variable lambda para analizar 
resultado=re.sub(patron,"*",cadena)
print(resultado)
os.system("Pause")