# def add_two_numbers(number_one, number_two):
#         resulta = number_one + number_two
#         print(resulta)
        
# add_two_numbers(3, 4)

# my_first_variable1 = 1  # my_first_variable bound to an integer object of value one.
# my_first_variable = 2  # my_first_variable re-assigned to integer value 2.

# print(type(my_first_variable))

# print(my_first_variable1)

# mi_primer_variable_int = 7
# mi_primer_variable_str = "Hola"

# print(type(mi_primer_variable_int))
# print(type(mi_primer_variable_str))

#Funciones //

# for i in range(65):
#      result = (2)**i
#      print(i, float(result))


# x = "Hola Este mensaje es para idenficar el lugar de las palabras"
# buscar_palabras = x[0:17]
# print(buscar_palabras)

# x = int(input("Ingresa tu codigo de estudiante: "))
# print(x)

# asignatura1 = float(input("Ingresa la calificacion de Matematicas: "))
# asignatura2 = float(input("Ingresa la calificacion de Fisica: "))
# asignatura3 = float(input("Ingresa la calificacion de Quimica: "))

# sum = asignatura1 + asignatura2 + asignatura3
# result = sum / 3

# if result >= 3.0:
#     print(round(result, 2), "Usted aprovo el area")
# else: 
#     print(round(result, 2), "Usted reprobo el area")

# x = int(input("Ingrese un numero entero del 1 al 5: "))


# if x == 1:
#     print("Uno")
    
# elif x == 2:
#     print("Dos")
    
# elif x == 3:
#     print("Tres")
    
# elif x == 4:
#     print("Cuatro")
    
# elif x == 5:
#     print("Sinco")
# else:
#     print("El valor no corresponde al sugerido...")
    
# print("Fin")



# print("Digta 1 si quieres convertir un numero en palabra: ")
# print("Digita 2 si quieres convertir una palabra en numero: ")

# opcion = int(input("Cual es tu opcion deseada: "))

# if opcion == 1:
#     num_let = int(input("Ingresa el numero que deseas convertir a palabra en un rango de 1 - 3: "))
#     if num_let == 1:
#         print("uno")
       
#     elif num_let == 2:
#         print("Dos")
        
#     elif num_let == 3:
#         print("Tres")
        
# elif opcion == 2:
#     let_num = str(input("Ingrese la palabra que quirea convertir a numero. Ejm 'Tres': ")) 
#     let_num = let_num.lower()
#     if let_num == "uno":
#         print(1)
        
#     elif let_num == "dos":
#         print(2)
        
#     elif let_num == "tres":
#         print(3)
        
# else:
#     opcion >= 3
#     print("Opcion no validad")

# x = int(input("Ingrese un numero mayor que 2 pero menor que 5: "))

# if x >= 2 and x <= 5: 
#     print(x, "Es mayor que 2 y menor que 5")
# elif x >= 5:
#     print(x, "Es mayor que 5")
    
# else:
#     x < 2
#     print("El valor no coincide")

# print("##### Bienvenido ##### \n")

# x = str(input("Digita tu nombre: "))
# print("Claves de departamentos: \n 1 = Atencion al cliente \n 2 = Logistica \n 3 = gerencia. \n")
# y = int(input("Digita tu clave de departamento: "))


# if y == 1:
#     print("Atencion al cliente")
#     y = int(input("Digita la cantidad de anos que has laborado con nosotros: "))
#     if y == 1:   
#         print(x, "Su periodo vacacional es de 6 dias!! ")
#     elif y == 2 or y <= 6:
#         print(x, "Su periodo vacacional consta de 14 dias habiles calendario!! ")
#     elif y >= 7:
#         print(x, "Su periodo vacacional consta de 20 dias habiles calendario!! ")
        
# elif y == 2:
#     print("Logistica")
#     y = int(input("Digita la cantidad de anos que has laborado con nosotros: "))
#     if y == 1:
#         print(x, "Su periodo vacacional consta de 7 dias habiles calendario!! ")
#     elif y == 2 or y <= 6:
#         print(x, "Su periodo vacacional consta de 15 dias habiles calendario!! ")
#     elif y >= 7:
#         print(x, "Su periodo vacacional consta de 22 dias habiles calendario!! ")
        
# elif y == 3:
#     print("Gerencia")
#     y = int(input("Digita la cantidad de anos que has laborado con nosotros: "))
#     if y == 1:
#         print(x, "Su periodo vacacional consta de 10 dias habiles calendario!! ")
#     elif y == 2 or y <= 6:
#         print(x, "Su periodo vacacional consta de 20 dias habiles calendario!! ")
#     elif y >= 7:
#         print(x, "Su periodo vacacional consta de 30 dias habiles calendario!! ")       
# else:
#  print("Clave Incorrecta")

# print("#### Programa que muestra si el numero es par o impar #####")
# print("###########################################################")

# x = int(input("Ingresa un numero entero: "))


# if x % 2 == 0:
#     print("par")
    
# elif x % 2 == 1:
#     print("Impar")

# print("#### Ver el numero mas alto de los entrantes. ####")

# x = int(input("Ingrese el primer  numero: "))
# y = int(input("Ingrese el segundo  numero: "))
# z = int(input("Ingrese el tercer  numero: "))

# if x > y and x > z:
#     print(x, "Es el numero mayor")
    
# elif y > x and y > z:
#     print(y, "Es el numero mayor")
    
# elif z > x and z > y:
#     print(z, "Es el numero mayor")
    
# else:
#     print("No coincide")

# x = input("Ingresa tu nombre: ")

# x += "  Este ejercicio corresponde a crecientes y decrecientes de los numeros."
# print(x)

# y = 1
 
# print("La variable y  empeiza con: = ", y)

# y +=1
# y +=1
# y +=1
# y +=1
# print("El creciente es ", y)

# z = 5 
# print("La variable z empieza por ", z)

# z -=1
# z -=1
# z -=1
# print("La variable z decrece: ", z)

print("#### Operaciones #####")

x = int(input("Presione el numero de la operacion que desea ejecutar, \n 1 = Suma \n 2 = Resta \n 3 = Multiplicacion \n 4 = Division : \n 5 = potencia \n 6 = Division con resultado de dos digitos \n"))

if x == 1:
    print("Usted escogio la Suma")
    suma = int(input("Ingrese un numero entero: "))
    suma1 = int(input("Ingrese un segundo numero entero: "))
    suma += suma1
    print("El resultado de la operacion es: ", suma)
    
elif x == 2:
    print("Ustd escogio la resta: ")
    resta = int(input("Ingrese un numero entero: "))
    resta1 = int(input("Ingrese un segundo numero entero: "))
    resta -= resta1
    print("El resutaldo de la resta es: ", resta)
    
elif x == 3:
    print("Ustd escogio la multiplicacion: ")
    mult = int(input("Ingrese un numero entero: "))
    mult1 = int(input("Ingrese un segundo numero entero: "))
    mult *= mult1
    print("El resutaldo de la multiplicacion es: ", mult)
    
elif x == 4:
    print("Ustd escogio la Divicion: ")
    div = int(input("Ingrese un numero entero: "))
    div1 = int(input("Ingrese un segundo numero entero: "))
    div /= div1
    print("El resutaldo de la Division es: ", div)
    
elif x == 5:
    print("Ustd escogio la Potencia: ")
    pote = int(input("Ingrese un numero entero: "))
    pote1 = int(input("Ingrese un segundo numero entero: "))
    pote **= pote1
    print("El resutaldo de la Division es: ", pote)
    
elif x == 6:
    print("Ustd escogio la Division con resultado de dos digitos no mas: ")
    divdedos = int(input("Ingrese un numero entero: "))
    divdedos1 = int(input("Ingrese un segundo numero entero: "))
    divdedos //= divdedos1
    print("El resutaldo de la Division es: ", divdedos)
    



    

    
    

    
    
    

    

        

        

    





