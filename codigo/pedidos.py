# Función para calcular el subtotal corrigiendo la incidencia INC-014
def calcular_subtotal(precio, cantidad):
    # Se corrige el error: ahora se multiplica el precio por la cantidad según la regla RN-01
    return precio * cantidad

# Variables de prueba solicitadas
precio = 80
cantidad = 3

# Llamada a la función para calcular el subtotal
subtotal = calcular_subtotal(precio, cantidad)

# Mostrar el resultado en pantalla (para S/ 80 y 3 unidades debe mostrar S/ 240)
print("Subtotal: S/", subtotal)