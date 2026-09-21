# ==========================================
# ESTADERO EL JOPO - SISTEMA DE CONTROL
# Módulo 4: Menú Interactivo y Control por Evento
# ==========================================

MENU = {
    "fria": 4500,
    "picada": 35000,
    "aguardiente": 90000,
    "gaseosa": 3500
}

NUM_MESAS = 3
PORCENTAJE_PROPINA = 0.10
PROPINA_MINIMA = 100000

# mostrar la carta oficial de el jopo
def mostrar_menu():
    print("\n--- MENÚ DE PRECIOS - EL JOPO ---")

    for producto, precio in MENU.items():
        print(f"  - {producto.capitalize()}: ${precio:,}")

    print("-" * 35)

# calcular el total de todas las mondades que pidieron en la mesa
def calcular_mesa(frias, picadas, aguardientes, gaseosa):
    subtotal = (
        (frias * MENU["fria"]) +
        (picadas * MENU["picada"]) +
        (aguardientes * MENU["aguardiente"])
        (gaseosa * MENU["gaseosa"])
    )

    propina = 0

    if subtotal >= PROPINA_MINIMA:
        propina = subtotal * PORCENTAJE_PROPINA

    total = subtotal + propina
    
    return subtotal, propina, total

#Imprime la liquidación de todas las mesas cargadas
def generar_reporte(historial_mesas):
    print("\n" + "=" * 45)
    print("        REPORTE GENERAL DE CAJA")
    print("=" * 45)

    total_ventas = 0
    total_propinas = 0

    for mesa, (subtotal, propina, total) in historial_mesas.items():
        total_ventas += subtotal
        total_propinas += propina
        print(f"Mesa #{mesa:02d} | Consumo: ${subtotal:9,.0f} | Propina: ${propina:7,.0f} | Total: ${total:9,.0f}")

    print("-"* 45)
    print(f"VENTAS TOTALES (Sin propina) : ${total_ventas:,.0f}")
    print(f"TOTAL PROPINAS RECAUDADAS   : ${total_propinas:,.0f}")
    print(f"GRAN TOTAL EN CAJA          : ${(total_ventas + total_propinas):,.0f}")
    print("=" * 45)

def registrar_pedido(mesas):
    num_mesa = int(input(f"Ingrese número de mesa (1-{NUM_MESAS}): "))      
    if 1 <= num_mesa <= NUM_MESAS:
        print(f"\n--- Registrar consumo Mesa #{num_mesa} ---")
        frias = int(input("¿Cuántas frías? "))
        picadas = int(input("¿Cuántas picadas? "))
        aguardientes = int(input("¿Cuántos aguardientes? "))
    
        subtotal, propina, total = calcular_mesa(frias, picadas, aguardientes)
        mesas[num_mesa] = (subtotal, propina, total)
        print(f"✔ Pedido cargado con éxito a la Mesa #{num_mesa}!")
    else:
        print("❌ Número de mesa inválido.")
       
# ------------------------------------------
# FLUJO PRINCIPAL INTERACTIVO
# ------------------------------------------
if __name__ == "__main__":
    # Inicializamos las 3 mesas en 0 usando un Diccionario de mesas
    # Estructura: { num_mesa: (subtotal, propina, total) }
    mesas = {i: (0, 0, 0) for i in range(1, NUM_MESAS + 1)}

    while True:
        print("\n=== SISTEMA DE SABOR - ESTADERO EL JOPO ===")
        print("1. Ver Carta de Precios")
        print("2. Registrar pedido a una Mesa")
        print("3. Consultar Estado de una Mesa")
        print("4. Ver Cierre / Reporte General")
        print("5. Salir del Sistema")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            mostrar_menu()

        elif opcion == "2":
            registrar_pedido(mesas)
        elif opcion == "3":
            num_mesa = int(input(f"Ingrese número de mesa a consultar (1-{NUM_MESAS}): "))
            if num_mesa in mesas:
                sub, prop, tot = mesas[num_mesa]
                print(f"\nEstado Mesa #{num_mesa:02d}: Consumo: ${sub:,.0f} | Propina: ${prop:,.0f} | Total: ${tot:,.0f}")
            else:
                print("❌ Número de mesa inválido.")

        elif opcion == "4":
            generar_reporte(mesas)

        elif opcion == "5":
            print("\nCerrando sistema... ¡Nos vemos en El Jopo!")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")