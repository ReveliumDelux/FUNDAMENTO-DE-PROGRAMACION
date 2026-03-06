// Algoritmo para calcular la potencia de un número
// Fórmula: resultado = base ^ exponente

Algoritmo CalcularPotencia
    // 1. DEFINICIÓN DE VARIABLES
    // nu: base de la potencia
    // n: exponente al que se eleva
    // resultado: guarda el producto final
    Definir nu, n Como Real
    Definir resultado Como Real // Eliminamos 'r' por no ser utilizada

    // 2. INTERFAZ DE USUARIO (ENTRADA)
    Escribir "--- Calculadora de Potencias ---" 
    Escribir ""
    
    Escribir Sin Saltar "Ingrese la base (número a multiplicar): "
    Leer nu
    
    Escribir Sin Saltar "Ingrese el exponente (potencia): "
    Leer n
    
    // 3. PROCESO (CÁLCULO)
    // El operador '^' eleva la base 'nu' al exponente 'n'
    resultado <- nu ^ n
    
    // 4. SALIDA DE DATOS
    Escribir ""
    // Corregimos el texto para que diga "resultado" en lugar de "valor del Trapecio"
    Escribir "El resultado de ", nu, " elevado a la ", n, " es: ", resultado 
    Escribir ""
    Escribir "------ Gracias por utilizar la calculadora de exponentes ------"
FinAlgoritmo
