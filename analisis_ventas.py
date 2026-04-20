
ventas = [
    {"fecha": "2024-01-01", "producto": "Manzana", "cantidad": 10, "precio": 1.5},
    {"fecha": "2024-01-01", "producto": "Banana", "cantidad": 5, "precio": 1.0},
    {"fecha": "2024-01-02", "producto": "Manzana", "cantidad": 8, "precio": 1.6},
    {"fecha": "2024-01-02", "producto": "Naranja", "cantidad": 12, "precio": 1.2},
    {"fecha": "2024-01-03", "producto": "Banana", "cantidad": 7, "precio": 1.1},
]

ingresos_totales = 0

for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print("Ingresos totales:", ingresos_totales)

ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]

    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

# encontrar el máximo
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

print("Producto más vendido:", producto_mas_vendido)
print("Cantidad total:", ventas_por_producto[producto_mas_vendido])

precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    if producto in precios_por_producto:
        suma_precios, total_cantidad = precios_por_producto[producto]
        suma_precios += precio * cantidad
        total_cantidad += cantidad
        precios_por_producto[producto] = (suma_precios, total_cantidad)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)

precio_promedio = {}

for producto, (suma, cantidad) in precios_por_producto.items():
    precio_promedio[producto] = suma / cantidad

print("Precio promedio por producto:", precio_promedio)

ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print("Ingresos por día:", ingresos_por_dia)
resumen_ventas = {}
for producto in ventas_por_producto:
    resumen_ventas[producto] = {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": precios_por_producto[producto][0],
        "precio_promedio": precio_promedio[producto]
    }
print("Resumen de ventas:", resumen_ventas)
with open("reporte_ventas.txt", "w", encoding="utf-8") as f:
    f.write("=== LISTA DE VENTAS ===\n")
    for v in ventas:
        f.write(str(v) + "\n")

    f.write("\n=== INGRESOS TOTALES ===\n")
    f.write(str(ingresos_totales) + "\n")

    f.write("\n=== PRODUCTO MÁS VENDIDO ===\n")
    f.write(f"{producto_mas_vendido}: {ventas_por_producto[producto_mas_vendido]}\n")

    f.write("\n=== PRECIO PROMEDIO ===\n")
    for k, v in precio_promedio.items():
        f.write(f"{k}: {v}\n")

    f.write("\n=== INGRESOS POR DÍA ===\n")
    for k, v in ingresos_por_dia.items():
        f.write(f"{k}: {v}\n")

    f.write("\n=== RESUMEN DE VENTAS ===\n")
    for k, v in resumen_ventas.items():
        f.write(f"{k}: {v}\n")