# Lista de notas
notas = []

# Introducir notas
while True:
    entrada = input("Introduce una nota (o escribe fin para terminar): ")

    if entrada.lower() == "fin":
        break

    nota = float(entrada)
    notas.append(nota)

# Mostrar estadísticas
if len(notas) > 0:

    print("Nota más alta:", max(notas))
    print("Nota más baja:", min(notas))
    print("Suma de las notas:", sum(notas))
    print("Número de notas:", len(notas))
    print("Nota media:", sum(notas) / len(notas))

    # Comprobar suspensos y ceros
    print("¿Hay algún suspenso?:", any(nota < 5 for nota in notas))
    print("¿No hay ningún cero?:", all(nota != 0 for nota in notas))

else:
    print("No se han introducido notas.")
