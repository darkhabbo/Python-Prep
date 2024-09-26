# Función para calcular la propina y el total a pagar
def calcular_propina():
    # Pedir al usuario que ingrese el valor de la cuenta y el porcentaje de propina
    valor_cuenta = float(input("Ingrese el valor de la cuenta: "))
    porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))
    
    # Calcular la propina
    propina = valor_cuenta * (porcentaje_propina / 100)
    
    # Calcular el total a pagar (cuenta + propina)
    total_a_pagar = valor_cuenta + propina
    
    # Mostrar los resultados
    print(f"La propina es: ${propina:.2f}")
    print(f"El total a pagar es: ${total_a_pagar:.2f}")

# Llamar a la función para ejecutar la calculadora
calcular_propina()
