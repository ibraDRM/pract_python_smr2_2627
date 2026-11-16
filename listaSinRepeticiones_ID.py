nombres = [
    "Alejandro", "Sofía", "Mateo", "Lucía", "Sebastián", "Valentina", "Daniel", "Martina",
    "Pablo", "María", "Álvaro", "Paula", "Adrián", "Julia", "Diego", "Valeria",
    "Javier", "Daniela", "Carlos", "Alba", "Lucas", "Emma", "Hugo", "Carla",
    "Martín", "Sara", "Manuel", "Carmen", "Pedro", "Noa", "David", "Claudia",
    "Mario", "Elena", "Marcos", "Irene", "Nicolás", "Nerea", "Gabriel", "Rocío",
    "Samuel", "Laura", "Gonzalo", "Marta", "Jorge", "Andrea", "Sergio", "Ana",
    "Luis", "Natalia", "Miguel", "Cristina", "Fernando", "Beatriz", "Raúl", "Patricia",
    "Rubén", "Silvia", "Iván", "Raquel", "Óscar", "Mónica", "Enrique", "Alicia",
    "Alberto", "Marina", "Víctor", "Inés", "Francisco", "Celia", "Antonio", "Nuria",
    "José", "Miriam", "Juan", "Lorena", "Andrés", "Eva", "Rafael", "Teresa",
    "Ramón", "Pilar", "Vicente", "Rosa", "Eduardo", "Ángela", "Ignacio", "Blanca",
    "Guillermo", "Clara", "Roberto", "Victoria", "Jaime", "Lidia", "Arturo", "Verónica",
    "Emilio", "Susana", "Tomás", "Isabel", "Héctor", "Yolanda", "César", "Sonia",
    "Julio", "Olga", "Salvador", "Carolina", "Agustín", "Vanesa", "Félix", "Gema",
    "Rodrigo", "Estefanía", "Iker", "Aitana", "Unai", "Laia", "Aitor", "Ane",
    "Biel", "Ona", "Pol", "Jana", "Arnau", "Abril", "Marc", "Iria",
    "Joel", "Nora", "Eric", "Vera", "Bruno", "Triana", "Leo", "Candela",
    "Gael", "Vega", "Thiago", "Alma", "Dylan", "Lola", "Enzo", "Jimena",
    "Darío", "Olivia", "Álex", "Chloe", "Ian", "Mía", "Oliver", "Zoe",
    "Alejandro", "Lucía", "Mateo", "María", "Daniel", "Sofía", "Pablo", "Paula",
    "Carlos", "Carmen", "Javier", "Laura", "Manuel", "Marta", "David", "Elena",
    "Lucas", "Sara", "Hugo", "Valeria", "Martín", "Alba", "Adrián", "Julia",
    "Diego", "Daniela", "Álvaro", "Martina", "José", "Ana", "Juan", "Isabel",
    "Antonio", "Cristina", "Francisco", "Patricia", "Miguel", "Beatriz", "Luis", "Silvia",
    "Alejandro", "María", "Lucía", "Carlos", "Sofía", "Daniel", "Paula", "Javier",
    "Carmen", "Manuel", "Laura", "David", "Marta", "Pablo", "Elena", "Mateo"
]


# VERSION 1: dejar una sola aparicion de cada nombre

nombresSinRepetir = []

for nombre in nombres:

    if nombre not in nombresSinRepetir:
        nombresSinRepetir.append(nombre)

print("Lista sin nombres repetidos:")
print(nombresSinRepetir)

print("Cantidad de nombres:", len(nombresSinRepetir))


# VERSION 2: eliminar todos los nombres que estan repetidos

nombresUnicos = []

for nombre in nombres:

    if nombres.count(nombre) == 1:
        nombresUnicos.append(nombre)

print("Lista sin ninguna aparicion de nombres repetidos:")
print(nombresUnicos)

print("Cantidad de nombres:", len(nombresUnicos))