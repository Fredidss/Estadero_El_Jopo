# Estadero El Jopo - Control de Gastos
# 12 clientes, cada fría vale $4.500

print("--- SISTEMA ESTADERO EL JOPO - CALLE 84 ---")

MENU = {
    "fria": 4500,
    "picada": 35000,
    "aguardiente": 45000,
    "gaseosa": 3500
}
VALOR_FRIA = 4500
NUM_MESAS = 12

historial_mesas = []    

for mesa in range(1, NUM_MESAS + 1):
    frias_consumidas = int(input(f"¿Cuántas frías consumió la mesa #{mesa}? "))
    consumo = frias_consumidas * VALOR_FRIA
    
    # Calculamos el consumo usando la clave del menú:
    consumo = frias_consumidas * MENU["fria"]
    
    print(f"\nMesa #{mesa}: {frias_consumidas} frías")

    if consumo >= 100000:
        propina = consumo * 0.10
        total_a_pagar = consumo + propina
        print(f"  Consumo: ${consumo:,.0f} COP")
        print(f"  Propina 10% incluida: ${propina:,.0f} COP")
        print(f"  TOTAL A PAGAR MESA {mesa}: ${total_a_pagar:,.0f} COP")
    else:
        total_a_pagar = consumo
        print(f"  Consumo: ${consumo:,.0f} COP")
        print(f"  No aplica propina (menos de $100.000)")
        print(f"  TOTAL A PAGAR MESA {mesa}: ${total_a_pagar:,.0f} COP")
    historial_mesas.append((mesa, frias_consumidas, total_a_pagar))

gran_total_dia = 0
for registro in historial_mesas:
    gran_total_dia += registro[2]
    
print(f"Total de mesas: {len(historial_mesas)}")
print(f"Gran total del día: ${gran_total_dia:,.0f} COP")
print("\n--- CIERRE DE CAJA EL JOPO ---")