"""
num1 = float(input("Ingrese su Primera nota del curso: "));
num2 = float(input("Ingrese su Segunda Nota del curso: "));
num3 = float(input("Ingrese su Tercera Nota del curso: "));
num4 = float(input("Ingrese su Cuarta Nota del curso: "));
num5 = float(input("Ingrese su Quinta Nota del curso: "));
num6 = float(input("Ingrese su sexta Nota del Curso: "));
num7 = float(input("Ingese su Septima Nota del Curso: "));

res = num1 + num2 + num3 + num4 + num5 + num6 + num7;
Resultado = res / 7
UnDigito = round(Resultado, 1)
if UnDigito >= 4.8:
    print("SU NOTA FINAL ES DE", UnDigito, "----")
    print("---Usted Aprobo el curso Correctamente Y estará participando para una Beca completa Universitaria---")

elif UnDigito >= 3:
    print("SU NOTA FINAL ES DE", UnDigito, "----")
    print("---Usted Aprobo el curso Correctamente---")
else:
    print("---Usted Reprobo el Curso, Nos vemos el Proximo Cuatrimeestre---")

print ("---GRACIAS POR UTILIZAR LA CALCULADORA DE NOTA FINAL")"""

edad = float(input("Intrudece la Edad: "));
if edad >= 18:
    print(f"Es mayor")
else 
    print(f"es menor")