# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=20):

    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Función principal interactiva
def main():
    # Pedir al usuario el monto total de la primera compra
    monto1 = float(input("Ingrese el monto total de la compra: $"))

    # Primera llamada con el descuento predeterminado (20%)
    descuento1 = calcular_descuento(monto1)
    print(f"Monto total: ${monto1:.2f}, Descuento: ${descuento1:.2f}, Monto final: ${monto1 - descuento1:.2f}")

    # Preguntar al usuario si desea usar un descuento diferente
    while True:
        usar_otro_descuento = input("¿Desea aplicar un porcentaje de descuento diferente? (sí/no): ")
        if usar_otro_descuento in ["sí", "si", "no"]:  # Acepta "si" sin tilde y "sí" con tilde
            break
        else:
            print("Por favor, responda 'sí', 'si' o 'no'.")

    if usar_otro_descuento in ["sí", "si"]:  # Acepta ambas formas
        # Pedir un segundo monto y porcentaje de descuento
        monto2 = float(input("Ingrese el monto total de la segunda compra: $"))
        porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (sin %): "))
        descuento2 = calcular_descuento(monto2, porcentaje_descuento)
        print(f"Monto total: ${monto2:.2f}, Descuento: ${descuento2:.2f}, Monto final: ${monto2 - descuento2:.2f}")
    else:
        print("No se aplicó un descuento diferente.")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
