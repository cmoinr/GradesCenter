import random
from werkzeug.security import generate_password_hash
from cs50 import SQL

# Conexión a la base de datos
db = SQL("sqlite:///gradescenter.db")

# Función para generar un ID único
def generar_id():
    return f"{random.randint(10000000, 99999999)}"

# Función para generar nombres aleatorios
def generar_nombre():
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Sofía", "Miguel", "Lucía", "Pedro", "Elena"]
    apellidos = ["García", "Rodríguez", "Martínez", "Hernández", "López", "González", "Pérez", "Sánchez", "Ramírez", "Torres"]
    return random.choice(nombres), random.choice(apellidos)

# Función para generar correos electrónicos
def generar_email(nombre, apellido):
    dominios = ["example.com", "mail.com", "test.com"]
    return f"{nombre.lower()}.{apellido.lower()}@{random.choice(dominios)}"

# Función para generar números de teléfono
def generar_telefono():
    return f"+58{random.randint(400, 499)}{random.randint(1000000, 9999999)}"

# Función para generar IDs de departamento aleatorios
def generar_departamento():
    departamentos = ["SE70", "ME02", "EC03", "DE04", "AG05", "SC06", "PO90"]  # IDs de departamentos existentes
    return random.choice(departamentos)

# Generar y llenar la tabla students
def generar_estudiantes(cantidad=1000):
    estudiantes = []
    for _ in range(cantidad):
        id_estudiante = generar_id()
        nombre, apellido = generar_nombre()
        contrasena = generate_password_hash("student")
        departamento = generar_departamento()
        email = generar_email(nombre, apellido)
        telefono = generar_telefono()

        estudiantes.append((id_estudiante, nombre, apellido, contrasena, departamento, email, telefono))

    # Insertar estudiantes en la base de datos
    for estudiante in estudiantes:
        db.execute("""
            INSERT INTO students (id, names, last_names, pw, department_id, email, phone)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, *estudiante)

    print(f"{cantidad} estudiantes generados e insertados en la base de datos.")

# Ejecutar la función
if __name__ == "__main__":
    generar_estudiantes()