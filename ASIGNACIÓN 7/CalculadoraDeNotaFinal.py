
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
if UnDigito >= 3:
    print (f"SU NOTA FINAL ES DE ", UnDigito," ---- ")
    print("---Usted Aprobo el curso Correctamente---")
else:
    print("---Usted Reprobo el Curso, Nos vemos el Proximo Cuatrimeestre---")

print ("---GRACIAS POR UTILIZAR LA CALCULADORA DE NOTA FINAL")

""" # Solicitar las 7 notas
notas = [float(input(f"Ingrese la nota {i + 1} del curso: ")) for i in range(7)]

# Calcular promedio
promedio = round(sum(notas) / len(notas), 1)

print(f"\nSu nota final es: {promedio}")

# Evaluar resultado
if promedio >= 4.8:
    print("¡Aprobado con excelencia! Participa por una beca completa universitaria.")
elif promedio >= 3:
    print("Aprobado correctamente.")
else:
    print("Reprobado. Nos vemos el próximo cuatrimestre.")

print("Gracias por utilizar la calculadora de nota final.") """