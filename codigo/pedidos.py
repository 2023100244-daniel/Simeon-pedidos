# Función para calcular el subtotal (RN-01)
def calcular_subtotal(precio, cantidad):
    return precio * cantidad

# Función para calcular el costo de envío según RN-02 y RN-03
def calcular_envio(subtotal):
    # RN-02: Si el subtotal es igual o superior a S/ 300, el envío es gratuito
    if subtotal >= 300:
        return 0
    # RN-03: Si el subtotal es inferior a S/ 300, el envío cuesta S/ 20
    else:
        return 20

# Casos de prueba
precio = 150
cantidad = 3

# Cálculos
subtotal = calcular_subtotal(precio, cantidad)
envio = calcular_envio(subtotal)
# RN-04: El total del pedido es el subtotal más el costo de envío
total = subtotal + envio

# Mostrar resultados
print("Subtotal: S/", subtotal)
print("Costo de envío: S/", envio)
print("Total del pedido: S/", total)