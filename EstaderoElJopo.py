# ==========================================
# ESTADERO EL JOPO - SISTEMA DE CONTROL
# Módulo 2: Menú Multiproducto y Cierre de Caja
# ==========================================

# Menú oficial (Diccionario Key: Value)
MENU = {
    "fria": 4500,
    "picada": 35000,
    "aguardiente": 90000,
    "gaseosa": 3500
}

NUM_MESAS = 2
historial_mesas = []

print("--- SISTEMA ESTADERO EL JOPO - CALLE 84 ---")
print("Menú de Precios:")
for producto, precio in MENU.items():
    print(f"  - {producto.capitalize()}: ${precio:,}")
print("-" * 43)

# Registro de consumos por mesa
for mesa in range(1, NUM_MESAS + 1):
    print(f"\n--- MESA #{mesa} ---")
    
    cant_frias = int(input("¿Cuántas frías consumió? "))
    cant_picadas = int(input("¿Cuántas picadas consumió? "))
    cant_aguardiente = int(input("¿Cuántos aguardientes consumió? "))
    
    # Cálculo subtotal usando los precios del diccionario MENU
    subtotal = (
        (cant_frias * MENU["fria"]) +
        (cant_picadas * MENU["picada"]) +
        (cant_aguardiente * MENU["aguardiente"])
    )
    
    # Evaluación de propina voluntaria / política del negocio
    if subtotal >= 100000:
        propina = subtotal * 0.10
    else:
        propina = 0
        
    total_mesa = subtotal + propina
    
    # Guardamos en la lista una tupla con el registro completo
    historial_mesas.append((mesa, subtotal, propina, total_mesa))

# ------------------------------------------
# REPORTE FINAL Y CIERRE DE CAJA
# ------------------------------------------
print("\n" + "=" * 43)
print("        REPORTE GENERAL DE CIERRE")
print("=" * 43)

total_ventas_dia = 0
total_propinas_dia = 0

# Unpacking de las tuplas guardadas en la lista
for mesa, subtotal, propina, total in historial_mesas:
    total_ventas_dia += subtotal
    total_propinas_dia += propina
    
    print(f"Mesa #{mesa:02d} | Consumo: ${subtotal:10,.0f} | Propina: ${propina:8,.0f} | Total: ${total:10,.0f}")

print("-" * 43)
print(f"VENTAS TOTALES (Sin propina) : ${total_ventas_dia:,.0f}")
print(f"TOTAL PROPINAS RECAUDADAS   : ${total_propinas_dia:,.0f}")
print(f"GRAN TOTAL EN CAJA          : ${(total_ventas_dia + total_propinas_dia):,.0f}")
print("=" * 43)