#Proyecto integrado pensamiento computacional
#Iker Alejandro Huidobro Muñoz A01752435
#Fryda Sofia Dolores Moran A01799451
#Yael Jhaid Leonardo Medina A01749832
import time #la utilizamos para el delay del programa
import os #la utilizamos para trabajar con el cls en auto
import datetime 

def funcion_break():
    while True:
        break

def compro_r(x):
    if x == 'exit':
        funcion_break() #llamamos a nuestra función para romper el ciclo
    while x.isdigit(): #verificamos que el str recibido sea una letra y no un número
        print("Formato de respuesta incorrecta")
        preguntas_espa_b() #volvemos a llamar a la función para volver a contestar las preguntas
    else:
        return x #si el formato de nuestra respuesta 

def seleccion():
    os.system('cls') #limpiamos la terminal
    x = input("Selecciona el área que quieres trabajar... l = lectura, m = matemáticas, c = ciencias; o escribe exit para salir: ") #menú para seleccionar el sector a trabajar
    if x == 'm': 
        mate() #llamamos a nuestra función de mate
    elif x == 'l':
        espa() #llamamos a nuestra función de lectura
    elif x == 'c':
        ciencias() #llamamos a nuestra función de ciencias
    else:  
        print("Comando incorrecto") #si la letra no corresponde marcamos error
    while x == 'exit':
        break #rompemos el ciclo si el usuario quiere salir

def recopila_datos():
    os.system('cls') #borramos la terminal
    ui = open("archivos-texto/user_info.txt","a") #abrimos nuestro archivo de texto
    nb = input("Cuál es tu nombre completo? ") #solicitamos el nombre
    aos = input("Cuántos años tienes? ") #solicitamos la edad
    ec = input("En qué escuela estudias? ") #solicitamos la escuela
    ui.write(f'-------------------------Usuario: {nb}--------------\n') #escribimos el nombre del usuario
    ui.write(f'Nombre completo: {nb} \n') #escribimos el nombre de nuestro usuario
    ui.write(f'Edad: {aos} \n') #escribimos la edad de nuestro usuario
    ui.write(f'Escuela en la que estudia: {ec} \n') #escribimos la escuela en la que estudia
    ui.close() #cerramos nuestro archivo de texto
    print("Información recopilada correctamente")
    seleccion() #vamos al menú de selección

def espa():
    os.system('cls') #limpiamos la terminal
    print("Bienvenido a la sección de Lectura, en esta tendrás que contestar 5 preguntas, conforme avances en el proceso irás subiendo de nivel según la cantidad de respuestas correctas que tengas")
    c = input("Presiona enter para continuar...")
    if c == "":
        os.system('cls')
        print("Pasando al sector de preguntas básicas...")   
        preguntas_espa_b() #entramos a la parte de preguntas fáciles
    else:
        print("Ingresa un comando válido")
    
def preguntas_espa_b():
    resp_c = ["a","a","d","b","b"] #nuestras respuestas
    pregs=open("archivos-texto/preguntas_espa_fa.txt",'r', errors="ignore") #abrimos nuestro archivo de texto
    pr=pregs.read() #leemos el archivo
    prl=pr.split('\n###\n') #separamos las preguntas
    pregs.close() #cerramos el archivo
    correctas=0  #contador de respuestas correctas
    incorrectas=0  #contador de respuestas incorrectas
    for k in range(len(prl)):
        response=input(f'{prl[k]}\nRespuesta: ') #realizamos la pregunta
        vr = compro_r(response) #mandamos a nuestra respuesta a la función encargada de comprobar el formato

        #si la respuesta concuerda con nuestra lista de respuestas entonces agregamos 1 a nuestro contador de respuestas correctas
        if vr==resp_c[k]: 
            print('Correcto')
            time.sleep(1)
            correctas += 1 
            os.system('cls')
       # de lo contrario entra al contador de respuestas incorrectas
        else:
            print('Incorrecto')
            time.sleep(1)
            incorrectas+=1
            os.system('cls')
    #abrimos nuestro archivo de la información del usuario
    ui = open("archivos-texto/user_info.txt","a")
    ui.write(f'Respuestas correctas en español básico: {correctas} \n') #agregamos las respuestas correctas que tuvo
    ui.write(f'Respuestas incorrectas en español básico: {incorrectas} \n') #agregamos las respuestas incorrectas que tuvo
    ui.write('-------------Intento nuevo o avance de sección-----------------\n')
    ui.close() 
    #imprimimos sus resultados
    print(f'Acabas de finalizar de contestar la sección básica de preguntas, obtuviste {correctas} de respuestas correctas y {incorrectas} de respuestas incorrectas')
    time.sleep(2)
    #el avance de nivel es automatizado, es decir, si obtiene más de 3 preguntas correctas, entonces pasa al siguiente nivel
    if correctas <= 3:
        print("Regresando al inicio...")
        time.sleep(1)
        seleccion()
    #de lo contrario regresa el incio para trabajar en otra materia o volver a intentarlo
    if correctas >= 3:
        c_o_m = input("Deseas continuar al siguiente nivel o regresar al inicio; Escribe inicio para regresar al menú o presiona enter para continuar")
        if c_o_m == 'inicio':
            seleccion()
        else:
            preguntas_espa_i()

def preguntas_espa_i(): #misma explicación que con def preguntas_espa_b():
    os.system('cls')
    print("Obtuviste más de 3 respuestas correctas en la parte básica por lo que ahora pasarás a la parte intermedia")
    resp_c = ["a","a","b","c","b"]
    pregs=open("archivos-texto/preguntas_espa_in.txt",'r', errors="ignore")
    pr=pregs.read()
    prl=pr.split('\n###\n')
    pregs.close()
    correctas=0 
    incorrectas=0
    for k in range(len(prl)):
        response=input(f'{prl[k]}\nRespuesta: ')
        vr = compro_r(response)

        if vr==resp_c[k]:
            print('Correcto')
            time.sleep(1)
            correctas += 1 
            os.system('cls')
        else:
            print('Incorrecto')
            time.sleep(1)
            incorrectas+=1
            os.system('cls') 
   
    ui = open("archivos-texto/user_info.txt","a")
    ui.write(f'Respuestas correctas en español intermedio: {correctas} \n')
    ui.write(f'Respuestas incorrectas en español intermedio: {incorrectas} \n')
    ui.write('-------------Intento nuevo o avance de sección-----------------\n')
    ui.close() 
    print(f'Acabas de finalizar de contestar la sección intermedia de preguntas, obtuviste {correctas} de respuestas correctas y {incorrectas} de respuestas incorrectas')
    time.sleep(2)
    if correctas <= 3:
        print("Regresando al inicio...")
        time.sleep(1)
        seleccion()
    if correctas >= 3:
        c_o_m = input("Deseas continuar al siguiente nivel o regresar al inicio; Escribe inicio para regresar al menú o presiona enter para continuar")
        if c_o_m == 'inicio':
            seleccion()
        else:
            preguntas_espa_a()

def preguntas_espa_a():#misma explicación que con def preguntas_espa_b():
    os.system('cls')
    print("Obtuviste más de 3 respuestas correctas en la parte básica por lo que ahora pasarás a la parte avanzada")
    resp_c = ["a","c","d","a","b"]
    pregs=open("archivos-texto/preguntas_espa_av.txt",'r', errors="ignore")
    pr=pregs.read()
    prl=pr.split('\n###\n')
    pregs.close()
    correctas=0 
    incorrectas=0
    for k in range(len(prl)):
        response=input(f'{prl[k]}\nRespuesta: ')
        vr = compro_r(response)

        if vr==resp_c[k]:
            print('Correcto')
            time.sleep(1)
            correctas += 1 
            os.system('cls')
        else:
            print('Incorrecto')
            time.sleep(1)
            incorrectas+=1
            os.system('cls') 
   
    ui = open("archivos-texto/user_info.txt","a")
    ui.write(f'Respuestas correctas en español avanzado: {correctas} \n')
    ui.write(f'Respuestas incorrectas en español avanzado: {incorrectas} \n')
    ui.write('-------------Intento nuevo o avance de sección-----------------\n')
    ui.close() 
    print(f'Acabas de finalizar de contestar la sección intermedia de preguntas, obtuviste {correctas} de respuestas correctas y {incorrectas} de respuestas incorrectas')
    time.sleep(2)
    print("Regresando al inicio...")
    time.sleep(1)
    seleccion()

def mate(): #misma explicación que con espa()
    os.system('cls')
    print("Bienvenido a la sección de Matemáticas, en esta tendrás que contestar 5 preguntas, conforme avances en el proceso irás subiendo de nivel según la cantidad de respuestas correctas que tengas")
    c = input("Presiona enter para continuar...")
    if c == "":
        os.system('cls')
        print("Pasando al sector de preguntas básicas...")   
        preguntas_mate_b() 
    else:
        print("Ingresa un comando válido")

def preguntas_mate_b():#misma explicación que con def preguntas_espa_b():
    resp_c = ["c","a","c","b","d"]
    pregs=open("archivos-texto/preguntas_mate_fa.txt",'r', errors="ignore")
    pr=pregs.read()
    prl=pr.split('\n###\n')
    pregs.close()
    correctas=0 
    incorrectas=0 
    for k in range(len(prl)):
        response=input(f'{prl[k]}\nRespuesta: ')
        vr = compro_r(response)

        if vr==resp_c[k]:
            print('Correcto')
            time.sleep(1)
            correctas += 1 
            os.system('cls')
        else:
            print('Incorrecto')
            time.sleep(1)
            incorrectas+=1
            os.system('cls')
   
    ui = open("archivos-texto/user_info.txt","a")
    ui.write(f'Respuestas correctas en matemáticas básico: {correctas} \n')
    ui.write(f'Respuestas incorrectas en matemáticas básico: {incorrectas} \n')
    ui.write('-------------Intento nuevo o avance de sección-----------------\n')
    ui.close() 
    print(f'Acabas de finalizar de contestar la sección básica de preguntas, obtuviste {correctas} de respuestas correctas y {incorrectas} de respuestas incorrectas')
    time.sleep(2)
    if correctas <= 3:
        print("Regresando al inicio...")
        time.sleep(1)
        seleccion()
    if correctas >= 3:
        c_o_m = input("Deseas continuar al siguiente nivel o regresar al inicio; Escribe inicio para regresar al menú o presiona enter para continuar")
        if c_o_m == 'inicio':
            seleccion()
        else:
            preguntas_mate_in()

def preguntas_mate_in():#misma explicación que con def preguntas_espa_b():

    resp_c = ["b","a","b","a","a"]
    pregs=open("archivos-texto/preguntas_mate_in.txt",'r', errors="ignore")
    pr=pregs.read()
    prl=pr.split('\n###\n')
    pregs.close()
    correctas=0 
    incorrectas=0 
    for k in range(len(prl)):
        response=input(f'{prl[k]}\nRespuesta: ')
        vr = compro_r(response)

        if vr==resp_c[k]:
            print('Correcto')
            time.sleep(1)
            correctas += 1 
            os.system('cls')
        else:
            print('Incorrecto')
            time.sleep(1)
            incorrectas+=1
            os.system('cls')
   
    ui = open("archivos-texto/user_info.txt","a")
    ui.write(f'Respuestas correctas en matemáticas intermedio: {correctas} \n')
    ui.write(f'Respuestas incorrectas en matemáticas intermedio: {incorrectas} \n')
    ui.write('-------------Intento nuevo o avance de sección-----------------\n')
    ui.close() 
    print(f'Acabas de finalizar de contestar la sección intermedia de preguntas, obtuviste {correctas} de respuestas correctas y {incorrectas} de respuestas incorrectas')
    time.sleep(2)
    if correctas <= 3:
        print("Regresando al inicio...")
        time.sleep(1)
        seleccion()
    if correctas >= 3:
        c_o_m = input("Deseas continuar al siguiente nivel o regresar al inicio; Escribe inicio para regresar al menú o presiona enter para continuar")
        if c_o_m == 'inicio':
            seleccion()
        else:
            preguntas_mate_av()
    
def preguntas_mate_av():#misma explicación que con def preguntas_espa_b():
    resp_c = ["d","c","c","b","a"]
    pregs=open("archivos-texto/preguntas_mate_av.txt",'r', errors="ignore")
    pr=pregs.read()
    prl=pr.split('\n###\n')
    pregs.close()
    correctas=0 
    incorrectas=0 
    for k in range(len(prl)):
        response=input(f'{prl[k]}\nRespuesta: ')
        vr = compro_r(response)

        if vr==resp_c[k]:
            print('Correcto')
            time.sleep(1)
            correctas += 1 
            os.system('cls')
        else:
            print('Incorrecto')
            time.sleep(1)
            incorrectas+=1
            os.system('cls')
   
    ui = open("archivos-texto/user_info.txt","a")
    ui.write(f'Respuestas correctas en matemáticas avanzadas: {correctas} \n')
    ui.write(f'Respuestas incorrectas en matemáticas avanzadas: {incorrectas} \n')
    ui.write('-------------Intento nuevo o avance de sección-----------------\n')
    ui.close() 
    print(f'Acabas de finalizar de contestar la sección básica de preguntas, obtuviste {correctas} de respuestas correctas y {incorrectas} de respuestas incorrectas')
    time.sleep(2)
    print("Regresando al inicio...")
    time.sleep(1)
    seleccion()

def ciencias(): #misma explicación que con espa()
    os.system('cls')
    print("Bienvenido a la sección de Ciencias, en esta tendrás que contestar 5 preguntas, conforme avances en el proceso irás subiendo de nivel según la cantidad de respuestas correctas que tengas")
    c = input("Presiona enter para continuar...")
    if c == "":
        os.system('cls')
        print("Pasando al sector de preguntas básicas...")   
        preguntas_ciencias_b() 
    else:
        print("Ingresa un comando válido")

def preguntas_ciencias_b(): #misma explicación que con def preguntas_espa_b():
    resp_c = ["a","d","c","a","b"]
    pregs=open("archivos-texto/preguntas_ciencias_fa.txt",'r', errors="ignore")
    pr=pregs.read()
    prl=pr.split('\n###\n')
    pregs.close()
    correctas=0 
    incorrectas=0 
    for k in range(len(prl)):
        response=input(f'{prl[k]}\nRespuesta: ')
        vr = compro_r(response)

        if vr==resp_c[k]:
            print('Correcto')
            time.sleep(1)
            correctas += 1 
            os.system('cls')
        else:
            print('Incorrecto')
            time.sleep(1)
            incorrectas+=1
            os.system('cls')
   
    ui = open("archivos-texto/user_info.txt","a")
    ui.write(f'Respuestas correctas en ciencias básico: {correctas} \n')
    ui.write(f'Respuestas incorrectas en ciencias básico: {incorrectas} \n')
    ui.write('-------------Intento nuevo o avance de sección-----------------\n')
    ui.close() 
    print(f'Acabas de finalizar de contestar la sección básica de preguntas, obtuviste {correctas} de respuestas correctas y {incorrectas} de respuestas incorrectas')
    time.sleep(2)
    if correctas <= 3:
        print("Regresando al inicio...")
        time.sleep(1)
        seleccion()
    if correctas >= 3:
        c_o_m = input("Deseas continuar al siguiente nivel o regresar al inicio; Escribe inicio para regresar al menú o presiona enter para continuar")
        if c_o_m == 'inicio':
            seleccion()
        else:
            preguntas_ciencias_in()

def preguntas_ciencias_in(): #misma explicación que con def preguntas_espa_b():
    resp_c = ["c","d","a","a","b"]
    pregs=open("archivos-texto/preguntas_ciencias_in.txt",'r', errors="ignore")
    pr=pregs.read()
    prl=pr.split('\n###\n')
    pregs.close()
    correctas=0 
    incorrectas=0 
    for k in range(len(prl)):
        response=input(f'{prl[k]}\nRespuesta: ')
        vr = compro_r(response)

        if vr==resp_c[k]:
            print('Correcto')
            time.sleep(1)
            correctas += 1 
            os.system('cls')
        else:
            print('Incorrecto')
            time.sleep(1)
            incorrectas+=1
            os.system('cls')
   
    ui = open("archivos-texto/user_info.txt","a")
    ui.write(f'Respuestas correctas en ciencias intermedio: {correctas} \n')
    ui.write(f'Respuestas incorrectas en ciencias intermedio: {incorrectas} \n')
    ui.write('-------------Intento nuevo o avance de sección-----------------\n')
    ui.close() 
    print(f'Acabas de finalizar de contestar la sección intermedia de preguntas, obtuviste {correctas} de respuestas correctas y {incorrectas} de respuestas incorrectas')
    time.sleep(2)
    if correctas <= 3:
        print("Regresando al inicio...")
        time.sleep(1)
        seleccion()
    if correctas >= 3:
        c_o_m = input("Deseas continuar al siguiente nivel o regresar al inicio; Escribe inicio para regresar al menú o presiona enter para continuar")
        if c_o_m == 'inicio':
            seleccion()
        else:
            preguntas_ciencias_av()

def preguntas_ciencias_av(): #misma explicación que con def preguntas_espa_b():
    resp_c = ["b","c","b","a","a"]
    pregs=open("archivos-texto/preguntas_ciencias_av.txt",'r', errors="ignore")
    pr=pregs.read()
    prl=pr.split('\n###\n')
    pregs.close()
    correctas=0 
    incorrectas=0 
    for k in range(len(prl)):
        response=input(f'{prl[k]}\nRespuesta: ')
        vr = compro_r(response)

        if vr==resp_c[k]:
            print('Correcto')
            time.sleep(1)
            correctas += 1 
            os.system('cls')
        else:
            print('Incorrecto')
            time.sleep(1)
            incorrectas+=1
            os.system('cls')
   
    ui = open("archivos-texto/user_info.txt","a")
    ui.write(f'Respuestas correctas en ciencias avanzado: {correctas} \n')
    ui.write(f'Respuestas incorrectas en ciencias avanzado: {incorrectas} \n')
    ui.write('-------------Intento nuevo o avance de sección-----------------\n')
    ui.close() 
    print(f'Acabas de finalizar de contestar la sección intermedia de preguntas, obtuviste {correctas} de respuestas correctas y {incorrectas} de respuestas incorrectas')
    time.sleep(2)
    print("Regresando al inicio...")
    time.sleep(1)
    seleccion()

def main(): #nuestro mensaje de entrada
    print("Cargando...")
    time.sleep(2)
    os.system('cls')
    #Iniciando el programa imprimimos un mensaje de bienvenida
    print("Bienvenido al programa de preparación para la PISA de la OCDE")
    print("En este programa vas a poder estudiar para tu examen PISA")
    print("Tendrás que contestar 5 preguntas de cada área integrada por Español,Matemáticas y Ciencias. \nCada sector consta de tres áreas, principiante, intermedio y avanzado")
    print(" ")
    c = input("Presiona enter para continuar...")
    if c == "":
        recopila_datos()  
    else: 
        print("Comando incorrecto, intenta de nuevo...") 


main()
