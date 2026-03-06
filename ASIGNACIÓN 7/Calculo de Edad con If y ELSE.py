# Pedimos al usuario que ingrese su edad.
# input() devuelve texto, por eso lo convertimos a número decimal con float().
edad = float(input("Introduce la Edad: "))

# Verificamos si la edad es mayor o igual a 18
if edad >= 18:
    # Si la condición es verdadera, se imprime este mensaje
    print("Es mayor")
else:
    # Si la condición es falsa (es menor de 18), se imprime este mensaje
    print("Es menor")