# ==========================================
# ESTADERO EL JOPO - SISTEMA DE CONTROL
# Módulo 3: Arquitectura Modular con Funciones
# ==========================================

MENU = {
    "fria": 4500,
    "picada": 35000,
    "aguardiente": 90000,
    "gaseosa": 3500
}

NUM_MESAS = 12


def mostrar_menu():
    """Muestra el menú oficial del estadero en pantalla."""
    print("--- SISTEMA ESTADERO EL JOPO - CALLE 84 ---")
    print("Menú de Precios:")
    for producto, precio in MENU.items():
        print(f"  - {producto.capitalize()}: ${precio:,}")
    print("-" * 43)


def calcular_mesa(frias, picadas, aguardientes):
    """
    Calcula subtotal, propina y total para una mesa.
    Retorna una tupla: (subtotal, propina, total)
    """
    subtotal = (
        (frias * MENU["fria"]) +
        (picadas * MENU["picada"]) +
        (aguardientes * MENU["aguardiente"])
    )
    
    # Propina del 10% si el subtotal alcanza los $100.000
    propina = subtotal * 0.10 if subtotal >= 100000 else 0
    total = subtotal + propina
    
    return subtotal, propina, total


def generar_reporte(historial):
    """Procesa e imprime el resumen final de caja."""
    print("\n" + "=" * 43)
    print("        REPORTE GENERAL DE CIERRE")
    print("=" * 43)

    total_ventas = 0
    total_propinas = 0

    for mesa, subtotal, propina, total in historial:
        total_ventas += subtotal
        total_propinas += propina
        print(f"Mesa #{mesa:02d} | Consumo: ${subtotal:10,.0f} | Propina: ${propina:8,.0f} | Total: ${total:10,.0f}")

    print("-" * 43)
    print(f"VENTAS TOTALES (Sin propina) : ${total_ventas:,.0f}")
    print(f"TOTAL PROPINAS RECAUDADAS   : ${total_propinas:,.0f}")
    print(f"GRAN TOTAL EN CAJA          : ${(total_ventas + total_propinas):,.0f}")
    print("=" * 43)


# ------------------------------------------
# FLUJO PRINCIPAL DE EJECUCIÓN
# ------------------------------------------
if __name__ == "__main__":
    mostrar_menu()
    historial_mesas = []

    for mesa in range(1, NUM_MESAS + 1):
        print(f"\n--- MESA #{mesa} ---")
        frias = int(input("¿Cuántas frías consumió? "))
        picadas = int(input("¿Cuántas picadas consumió? "))
        aguardientes = int(input("¿Cuántos aguardientes consumió? "))

        subtotal, propina, total = calcular_mesa(frias, picadas, aguardientes)
        historial_mesas.append((mesa, subtotal, propina, total))

    generar_reporte(historial_mesas)