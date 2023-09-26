maxf = 3
maxc = 5
a = [[0] * maxc for _ in range(maxf)]

# Escribir el array
for f in range(maxf):
    for c in range(maxc):
        print("Ingreseo el valor:")
        a[f][c] = int(float(input()))

# Leer el array
print("Los valores del arreglos son los siguientes:")
for f in range(maxf):
    for c in range(maxc):
        print(a[f][c], end=" ")
    print()

