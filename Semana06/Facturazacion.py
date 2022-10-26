# Dado el subtotal calcular el igv del total

import Financieros

subtotal=800.77

print(f"Subtotal : {subtotal}")
print(f"IGV: {Financieros.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"Total: {Financieros.obtenerTotalconSubtotal(subtotal): .2f}") 