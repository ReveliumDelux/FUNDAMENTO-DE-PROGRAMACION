Algoritmo CalculadoraNota

    Definir n1, n2, n3, n4, n5, n6, n7 Como Real
    Definir resultado, dosdigitos Como Real 

    // 2. INTERFAZ DE USUARIO (ENTRADA)
    Escribir "--- Calculadora de Potencias ---" 
    Escribir ""
    Escribir "Debera Ingresar las notas con el punto DecimaL (.)"
    Escribir "El Promedio tendrá una evaluación de 1.0 a 5.0 para calcular la aprobación del Curso"
    Escribir ""
    Escribir Sin Saltar "Ingrese su Primera Nota: "
    Leer n1
    Escribir Sin Saltar "Ingrese su Segunda Nota: "
    Leer n2
    Escribir Sin Saltar "Ingrese su Tercera Nota: "
    Leer n3
    Escribir Sin Saltar "Ingrese su Cuarta Nota: "
    Leer n4
    Escribir Sin Saltar "Ingrese su Quinta Nota: "
    Leer n5
    Escribir Sin Saltar "Ingrese su Sexa Nota: "
    Leer n6
    Escribir Sin Saltar "Ingrese su Septima Nota: "
    Leer n7
    resultado<-(n1+n2+n3+n4+n5+n6+n7)/7
    dosdigitos <- redon(resultado * 10) / 10 
    Escribir ""
    Escribir "El resultado de su Nota Final es de: ", dosdigitos

    Si resultado >= 3.0 Entonces
        Escribir "El estudiante APROBÓ el Curso."
        Sino
            Escribir "El Estudiante REPROBÓ el Curso, Nos vemos el próximo Cuatrimestre."
    FinSi

    Escribir ""
    Escribir "------ Gracias por utilizar la calculadora de exponentes ------"
FinAlgoritmo
 

