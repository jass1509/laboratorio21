class OperadorInvalido(Exception):
    pass

operacion = input("ingrese la operación  ")

try:
    # separar componentes
    partes = operacion.split()

    if len(partes) != 3:
        raise ValueError("formato incorrecto")

    num1_str, operador, num2_str = partes

    # convertir a float
    numero1 = float(num1_str)
    numero2 = float(num2_str)

    # validar operador
    if operador not in ["+", "-", "*", "/"]:
        raise OperadorInvalido("Operador no valido")

    # realizar operación
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2

    print("El resultado es:", resultado)

except ZeroDivisionError:
    print("Error, no se puede dividir entre cero")

except ValueError:
    print("Error: valores invalidos")

except OperadorInvalido as e:
    print("Error:", e)
