# Elias Amaru Carreño Arriagada 22.382.218-5
# INGRESAR SUS NOMBRES COMPLETOS Y SUS RUTS AQUI PORFAVOR.
# Benedick Anthony Mamani Mamani 27.608.499-2

#🙌🙌🙌Agrege esta variable glovales
plan_impresion = []
PRECIO_REVISTA = 3820  # Precio por revista según el enunciado
MAX_IMPRESIONES = 2300  # Máximo de impresiones por día según el enunciado

def interfaz_menu():
    print("\nMENÚ\n") ##🙌🙌🙌Agrege esto para que sea igual a el ejemplo de la tarea
    print("""SISTEMA DE PLANIFICACIÓN DE IMPRESIÓN DE REVISTAS ESPECIALIZADAS\n
1. Generar plan de impresión
2. Ingresar cantidad de impresiones por revista especializada y día
3. Visualizar el ingreso total de una revista especializada específica
4. Visualizar el ingreso total de todas las revistas especializadas en un día específico
5. Salir del programa\n""")
# Utilizamos el comando "\n" para separar el texto y que sea más agradable a la vista del usuario.
# Interfaz del menu solicitado, trabajaremos todas las opciones con funciones que seran llamadas con  la variable "opcion".

def generar_impresion():
    print("\nGenerar plan de impresión\n") #🙌🙌🙌Agrege un "\n"
    num_revistas = int(input("Ingrese número de tipos de revistas especializadas: "))
    num_dias = int(input("Ingrese número de días de impresión: "))
    # 🙌🙌🙌borre el "plan_impresion = []", porque ya esta como global
    for i in range(num_revistas):
        # Cada fila es una revista y cada columna un dia.
        plan_impresion.append([0]*num_dias)
        # Esta linea de codigo crea una lista de "num_dias" elementos, y cada uno de esos elementos es el número 0.
    print("\nPlan de impresión inicial:") #🙌🙌🙌Retrocedi un espacio para que no se repita
    mostrar_plan_impresion() #🙌🙌🙌 Agrege la funcion para mostar el plan 

def ingresar_impresiones(): #🙌🙌🙌Cree la funcion correcpondiente a la opcion 2
     #🙌🙌🙌Genera un for para que pida ingresar varias veses un for, hasta que todos tengan un valor
    for i in range(len(plan_impresion)):  #🙌🙌🙌 Coloque un len para que cada ves que repira i aumente en 1
        print(f"\nRevista {i + 1}")
        for j in range(len(plan_impresion[i])):  #🙌🙌🙌J es la fila de las revistas
            while True:
                cantidad = int(input(f"Ingrese cantidad de revistas a imprimir en el día {j + 1}: "))
                if cantidad < 0: #🙌🙌🙌En caso de que sea 0 o menor
                    print("Ingresaste un valor negativo, intente otra vez")
                elif cantidad > MAX_IMPRESIONES:  #🙌🙌🙌En caso de que supere el limite
                    print(f"Superaste el limite de las impreciones {MAX_IMPRESIONES}, intenta otra vez")
                else:  
                    plan_impresion[i][j] = cantidad  #🙌🙌🙌Modifica el valor de esa cordenada 
                    break
    mostrar_plan_impresion() # #🙌🙌🙌 Despues de colocar los valores, imprimira el plan

def mostrar_plan_impresion(): #🙌🙌🙌La funcion es para solo tener que llamar a la funccion en vez de tener que imprimir en cada funcion por separado
    
    print("\nPlan de impresión:")
    print("*" * 50)

    print("      Dia: ", end="")  #🙌🙌🙌El end hace que despues del print no salte de linea
     #🙌🙌🙌 (1, len(plan_impresion[0]) + 1). el primer 1 es para que cuente los dias desde 1 y no 0 "por defecto"
     #len para que dia aumente con cada ciclo
     #[0] para que empize por la primera fila "revista"
     #+1 es para que incluya el ultimo valor de la fila "por defecto no la incluye"
    for dia in range(1, len(plan_impresion[0]) + 1): #🙌🙌🙌Hace que imprima dia: 1,2,3 etc
        print(f"{dia:^8}", end="") #🙌🙌🙌 el elevado a 8 espara que el plan este organizado y ocupe un espacio correspondiente

    for i, revista in enumerate(plan_impresion, 1): #🙌🙌🙌El enumerate hace que el len afecte a i y a revista a la vez 
        print(f"\nRevista {i}: ", end="")
        for cantidad in revista:
            # Centrar las cantidades dentro de un espacio de 8 caracteres
            print(f"{cantidad:^8}", end="")

    print("\n" + "*" * 50)


while True:
    interfaz_menu()
    opcion = int(input("Seleccione su opción: "))

    if opcion == 1:
        generar_impresion()
    
    elif opcion == 2:
        ingresar_impresiones() #🙌🙌🙌Agrege que llamara la funcion
        pass
    
    elif opcion == 3:
        #funcion3() PENDIENTE CREAR
        pass
    
    elif opcion == 4:
        #funcion4() PENDIENTE CREAR
        pass
    
    elif opcion == 5:
        break
    
    else:
        print("La Opcion es Invalida, intentelo denuevo.")
