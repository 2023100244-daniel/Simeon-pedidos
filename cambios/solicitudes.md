Registro de Solicitudes y Evaluación de Impacto

Solicitud: INC-014
* Descripción: El sistema devuelve el precio unitario como subtotal, sin considerar la cantidad solicitada[cite: 1].
* Tipo de cambio: Corrección de error (Incidencia).
* Justificación: El cálculo actual es incorrecto y afecta los ingresos, ya que no se está multiplicando por la cantidad de productos solicitados.
* Requisito asociado: RN-01 (El subtotal es el precio unitario multiplicado por la cantidad)[cite: 1].
* Archivos afectados: codigo/pedidos.py.
* Riesgo: Bajo. El cambio se limita a una sola línea matemática en la función principal.
* Criterio de aceptación: Al ejecutar el programa con un precio de S/ 80 y 3 unidades, el subtotal devuelto debe ser de S/ 240[cite: 1].
* Decisión de aprobación simulada: Aprobado.

---

Solicitud: CR-015
* Descripción: La gerencia solicita incorporar el cálculo automático del costo de envío y el total del pedido[cite: 1].
* Tipo de cambio: Nueva funcionalidad (Feature).
* Justificación: Es necesario para el negocio poder cobrar o exonerar automáticamente el costo de envío según el monto de la compra.
* Requisito asociado: RN-02, RN-03 y RN-04[cite: 1].
* Archivos afectados: codigo/pedidos.py y documentos/requisitos.md[cite: 1].
* Riesgo: Medio. Requiere agregar lógica condicional para evaluar si el envío es gratuito o tiene un costo de S/ 20[cite: 1].
* Criterio de aceptación: El programa debe mostrar correctamente el subtotal, costo de envío y total del pedido según la tabla de casos de prueba (ej. para S/ 100 x 3, envío debe ser S/ 0 y total S/ 300)[cite: 1].
* Decisión de aprobación simulada: Aprobado.