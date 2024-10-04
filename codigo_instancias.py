import random

def generar_instancias(num_asignaturas, num_salas, num_profesores):
    
    # Generar asignaturas
    asignaturas = []
    asig_1_bloque = int(0.65 * num_asignaturas)
    for i in range(num_asignaturas):
        # Por cada 5 asignaturas, 1 es indispensable
        if i % 5 == 0:
            es_indispensable = 1  
        else:
            es_indispensable = 0

        if es_indispensable:
            prioridad = random.randint(6, 10)  # Prioridad de 6 a 10 para indispensables
        else:
            prioridad = random.randint(1, 5)  # Prioridad de 1 a 5 para otros

        # Determinar bloques necesarios: 65% de las asignaturas con 1 bloque, el resto con 2
        if i < asig_1_bloque:
            bloques_necesarios = 1
        else:
            bloques_necesarios = 2  
            
        interes_estudiantes = random.randint(10, 40)  # Número de estudiantes interesados
        
        # Se guardan las caracteristicas de las asignaturas en un arreglo que contiene los elementos de este
        asignaturas.append({'id': i + 1, 'indispensable': es_indispensable, 'prioridad': prioridad, 'bloques_necesarios': bloques_necesarios, 'interes_estudiantes': interes_estudiantes})

    # Generar profesores
    profesores = []
    for p in range(num_profesores):
        # El profesor tiene entre 14 y 28 bloques disponibles de un total de 35 bloques posibles
        bloques_disponibles = random.sample(range(1, 35), random.randint(14, 28))

        # Se guardan las caracteristicas de los profesores en un arreglo que contiene los elementos de este
        profesores.append({ 'id': p + 1, 'bloques_disponibles': bloques_disponibles})
    
    # Generar salas con capacidad
    salas = []
    for z in range(num_salas):
        capacidad = random.randint(20, 45)  # Capacidad entre 20 y 45 estudiantes
        salas.append({ 'id': z + 1, 'nombre': f"Sala_{z + 1}", 'capacidad': capacidad })

    # Retornar las instancias generadas
    return asignaturas, profesores, salas

# Funcion para mostrar instancias generadas
def print_instancias(asignaturas, salas, profesores):
    
    print("Asignaturas generadas:")
    for asignatura in asignaturas:
        print(f"Asignatura {asignatura['id']}: Indispensable = {asignatura['indispensable']}, "
            f"Prioridad = {asignatura['prioridad']}, Bloques necesarios = {asignatura['bloques_necesarios']}, "
            f"Interés estudiantes = {asignatura['interes_estudiantes']}")

    print("\nProfesores generados:")
    for p in profesores:
        print(f"Profesor {p['id']}: Bloques disponibles = {p['bloques_disponibles']}")

    print("\nSalas generadas:")
    for sala in salas:
        print(f"Sala {sala['nombre']}: Capacidad = {sala['capacidad']} estudiantes")
        return


# Crear instancias
# Instancia pequeña
num_asignaturas = 10 
num_salas = 1 
num_profesores = 2 

asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# Instancias mediana

# 1
num_asignaturas = random.randint(40, 45)
num_salas = 3
num_profesores = 6
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# 2
num_asignaturas = random.randint(54, 58)
num_salas = 4
num_profesores = 8
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# 3
num_asignaturas = random.randint(68, 72)
num_salas = 5
num_profesores = 10
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# 4
num_asignaturas = random.randint(80, 85)
num_salas = 6
num_profesores = 12
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# 5
num_asignaturas = random.randint(95, 99)
num_salas = 7
num_profesores = 14
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# Instancias grandes

# 1
num_asignaturas = random.randint(180, 200)
num_salas = random.randint(9, 11)
num_profesores = 28    
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# 2
num_asignaturas = random.randint(210, 230)
num_salas = random.randint(12, 14)
num_profesores = 32   
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# 3
num_asignaturas = random.randint(250, 270)
num_salas = random.randint(15, 17)
num_profesores = 36   
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# 4
num_asignaturas = random.randint(300, 320)
num_salas = random.randint(18, 20)
num_profesores = 40   
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)

# 5
num_asignaturas = random.randint(340, 360)
num_salas = random.randint(21, 23)
num_profesores = 44   
asignaturas, profesores, salas = generar_instancias(num_asignaturas, num_salas, num_profesores)
