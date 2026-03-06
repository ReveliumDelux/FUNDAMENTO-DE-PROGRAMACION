while True:
    try:
        dia_num = int(input("Introduzca un número (1 - 7): "))

        if 1 <= dia_num <= 7:
            match dia_num:
                case 1:
                    print("Lunes")
                case 2:
                    print("Martes")
                case 3:
                    print("Miércoles")
                case 4:
                    print("Jueves")
                case 5:
                    print("Viernes")
                case 6:
                    print("Sábado")
                case 7:
                    print("Domingo")
            break  # Sale del bucle si el número es correcto
        else:
            print("Número inválido. Debe estar entre 1 y 7.")

    except ValueError:
        print("Error: Debe introducir un número entero.")