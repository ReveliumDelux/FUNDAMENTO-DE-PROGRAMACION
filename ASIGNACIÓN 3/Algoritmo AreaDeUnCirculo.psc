Proceso 

Algoritmo AreaDeUnCirculo
	
Definir area, r Como REAL
Definir PI Como REAL

	Escribir "---Estamos Calculando el Área de un Circulo---" 
	Escribir ""
	Mientras PI <> 3.1416 Hacer
		Escribir "POR FAVOR INGRESAR LOS SIGUIENTES DÍGITOS (3.1416) PARA PODER CONTINUAR:"
		Leer PI
		
		Si pi_usuario <> 3.1416 Entonces
			Escribir "Valor incorrecto. Asegúrese de usar el punto decimal (.)."
		FinSi
	FinMientras
	Escribir "¡Su Validación a sido exitosa!"
	Escribir ""
	Escribir Sin Saltar "Ingrese eL Radio de su Circunferencia:  "
	Leer r
	Escribir ""
	area<- PI*(r^2) // Calcula el área multiplicando Pi por el radio elevado al cuadrado, El area esta definida para arrojar el resultado de el dato PI que es una constante luego se utiliza una multiplicación que señalamos el radio que nos brinda el usuario al cuadrado para así arrojar el resultado de la formula aplicada. Como NO podemos ingresar pi, lo que hicimos fue pedirle al usuario que lo ingresara con un ciclo para que Sino cumple los requisitos el fron le enviara una alerta que debe colocar el punto decimal. 
	Escribir ""
    Escribir "El valor del Área con PI es de: ", area
	Escribir "------Gracias por Utilizarme ésta calculadora de Circunferencia ------"
FinProceso

 
