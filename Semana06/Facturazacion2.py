import Financieros

total=1000.49

print(f"Subtotal: {Financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {Financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")