#hola mundo
print ("Hola mundo!")
print ("Me esta gustando Python")
nombre = input("Dime como te llamas: ")
apellido = input("Ingresa tu apellido: ")
print(f"hola {nombre} {apellido}. bienvenido a la plataforma")
edad = input("ingresa tu edad: ")
ciudad = input("En que ciudad vives? ")
print("quedas registrado en tu plataforma")
print(f"User:{nombre} {apellido}, edad {edad} {ciudad}, ya puedes ingresas.")
print("Que quieres sumar?:")
# Función para realizar la suma
def sumar(x, y):
    return x + y
# Solicitar al usuario que ingrese los dos números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
# Calcular la suma
resultado = sumar(numero1, numero2)
# Mostrar el resultado
print("El resultado de la suma es:", resultado)