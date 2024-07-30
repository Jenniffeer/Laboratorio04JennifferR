#Problema 1: Clasificar una calificación.

def clasificar_calificacion(calificacion):
    if 90 <= calificacion <= 100:
        return 'A'
    elif 80 <= calificacion <= 89:
        return 'B'
    elif 70 <= calificacion <= 79:
        return 'C'
    elif 60 <= calificacion <= 69:
        return 'D'
    elif 0 <= calificacion <= 59:
        return 'F'
    else:
        return 'Calificación inválida'

def main():
    while True:
        entrada = input("Ingresa una calificación numérica entre 0 y 100 (o 'S' para salir): ").strip()
        
        if entrada.upper() == 'S':
            print("Saliendo del programa...")
            break
        
        try:
            calificacion = int(entrada)
            if 0 <= calificacion <= 100:
                clasificacion = clasificar_calificacion(calificacion)
                print(f"La calificación {calificacion} corresponde a la letra {clasificacion}.")
            else:
                print("Por favor, ingresa un número entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entre 0 y 100 o 'S' para salir.")

if __name__ == "__main__":
    main()


#Problema 2: Determinar el tipo de triángulo según las longitudes de sus lados.
def determinar_tipo_triangulo(lado1, lado2, lado3):

    if lado1 == lado2 == lado3:
        return 'Equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'Isósceles'
    else:
        return 'Escaleno'

def main():
    while True:
        entrada = input("Ingresa las longitudes de los tres lados del triángulo separados por espacios (o 'S' para salir): ").strip()
        
        if entrada.upper() == 'S':
            print("Saliendo del programa...")
            break
        
        try:
            lados = list(map(float, entrada.split()))
            
            if len(lados) != 3:
                print("Por favor, ingresa exactamente tres valores numéricos.")
                continue
            
            lado1, lado2, lado3 = lados
            
            if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                print("Las longitudes de los lados deben ser mayores que 0.")
                continue
            
            if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
                tipo_triangulo = determinar_tipo_triangulo(lado1, lado2, lado3)
                print(f"El triángulo con lados {lado1}, {lado2}, {lado3} es {tipo_triangulo}.")
            else:
                print("Las longitudes ingresadas no forman un triángulo válido.")
                
        except ValueError:
            print("Entrada no válida. Por favor, ingresa tres números separados por espacios o 'S' para salir.")

if __name__ == "__main__":
    main()



#Problema 3: Calcular el precio del boleto de cine según la edad.

def calcular_precio_boletos(edades):
    total = 0
    for edad in edades:
        if edad < 12:
            total += 5
        elif 13 <= edad <= 18:
            total += 7
        elif edad > 65:
            total += 6
        else:
            total += 10

    if len(edades) > 3:
        total *= 0.9  # Aplicar un descuento del 10%

    return total

def main():
    while True:
        entrada = input("Ingresa la cantidad de personas y sus edades separadas por espacios (o 'S' para salir): ").strip()
        
        if entrada.upper() == 'S':
            print("Saliendo del programa...")
            break
        
        try:
            datos = list(map(int, entrada.split()))
            
            if len(datos) < 2:
                print("Por favor, ingresa la cantidad de personas y al menos una edad.")
                continue
            
            cantidad_personas = datos[0]
            edades = datos[1:]
            
            if len(edades) != cantidad_personas:
                print("El número de edades ingresadas no coincide con la cantidad de personas.")
                continue
            
            precio_total = calcular_precio_boletos(edades)
            print(f"El precio total del boleto para {cantidad_personas} personas es: ${precio_total:.2f}")
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa números enteros separados por espacios o 'S' para salir.")

if __name__ == "__main__":
    main()


#Problema 4: Imprimir números pares en un rango dado.
def imprimir_pares(inicio, fin):
    if inicio >= fin:
        print("El número de inicio debe ser menor que el número de fin")
        return
    
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            print(numero)

def main():
    while True:
        entrada = input("Ingresa dos números enteros inicio y fin (o 'S' para salir): ").strip()
        
        if entrada.upper() == 'S':
            print("Saliendo del programa...")
            break
        
        try:
            inicio, fin = map(int, entrada.split())
            imprimir_pares(inicio, fin)
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa dos números enteros separados por un espacio o 'S' para salir.")

if __name__ == "__main__":
    main()


#Problema 5: Calcular sumatoria de números.
"Escribe un programa que solicite al usuario ingresar dos números enteros inicio y fin"
def calcular_sumatoria(n):
    if n <= 0:
        print("El número ingresado no es válido")
        return
    
    sumatoria = 0
    for numero in range(1, n + 1):
        sumatoria += numero
    
    print(f"La sumatoria de los números de 1 hasta {n} es: {sumatoria}")

def main():
    while True:
        entrada = input("Ingresa un número entero positivo n (o 'S' para salir): ").strip()
        
        if entrada.upper() == 'S':
            print("Saliendo del programa...")
            break
        
        try:
            n = int(entrada)
            calcular_sumatoria(n)
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero positivo o 'S' para salir.")

if __name__ == "__main__":
    main()


#Problema 6: Suma de números hasta que se ingrese un número negativo
def suma_numeros_positivos():
    suma_total = 0
    cantidad_numeros = 0

    while True:
        entrada = input("Ingresa un número entero positivo (o un número negativo para salir): ").strip()
        
        try:
            numero = int(entrada)
            
            if numero < 0:
                print(f"Suma total de los números positivos ingresados: {suma_total}")
                print(f"Cantidad de números ingresados: {cantidad_numeros}")
                break
            
            suma_total += numero
            cantidad_numeros += 1
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    suma_numeros_positivos()
