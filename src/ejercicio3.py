import pandas as pd

cuad1 = pd.read_csv("datos/vendas_2025_cuadrimestre1.csv", sep=";", decimal=",")
cuad2 = pd.read_csv("datos/vendas_2025_cuadrimestre2.csv", sep=";", decimal=",")
cuad3 = pd.read_csv("datos/vendas_2025_cuadrimestre3.csv", sep=";", decimal=",")

numero_ventas = cuad1["id_venda"].count() + cuad2["id_venda"].count() + cuad3["id_venda"].count()

importe_total = cuad1["importe"].sum() + cuad2["importe"].sum() + cuad3["importe"].sum()

ventas_format = f"{numero_ventas:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
importe_format = f"{importe_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print("Número de ventas:", ventas_format)
print(f"Importe total: {importe_format} €")