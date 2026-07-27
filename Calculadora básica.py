Introduzca_un_numero = (input("Introduzca un numero: "))
simbolos = ["+", "-", "*", "/", "**"]
print(f"Seleccione una operacion: {simbolos} ")
input_operacion = input("Introduzca la operacion: ")
Introduzca_otro_numero = (input("Introduzca otro numero: "))

if "/" in Introduzca_un_numero:
    Introduzca_un_numero.split("/")
    partes_1= Introduzca_un_numero.split("/")
    Introduzca_un_numero = float(partes_1[0])/float(partes_1[1])
else:
    Introduzca_un_numero = float(Introduzca_un_numero)
    
if "/" in Introduzca_otro_numero:
    Introduzca_otro_numero.split("/")
    partes_2= Introduzca_otro_numero.split("/")
    Introduzca_otro_numero = float(partes_2[0])/float(partes_2[1])
else:
    Introduzca_otro_numero = float(Introduzca_otro_numero)

if input_operacion == "+":
    resultado = Introduzca_un_numero + Introduzca_otro_numero
elif input_operacion == "-":
    resultado = Introduzca_un_numero - Introduzca_otro_numero
elif input_operacion == "*":
    resultado = Introduzca_un_numero * Introduzca_otro_numero
elif input_operacion == "/":
    resultado = Introduzca_un_numero / Introduzca_otro_numero
elif input_operacion == "**":
    resultado = Introduzca_un_numero ** Introduzca_otro_numero
else:
    resultado = "Operacion no valida"

    


print(f"El resultado de la operacion es: {resultado}")