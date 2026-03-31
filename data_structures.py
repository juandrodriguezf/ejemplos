# === ESTRUCTURAS DE DATOS EN PYTHON ===

def ejemplificar_listas():
    # 1. LISTAS (Mutables, Ordenadas)
    # Útiles cuando necesitas una colección de elementos que se pueden modificar.
    frutas = ["Manzana", "Banano", "Cereza"]
    frutas.append("Damasco") # Agregar elemento
    frutas[0] = "Manzana Roja" # Modificar elemento
    print(f"\n[LISTAS]: {frutas}")
    print(f"La primera es: {frutas[0]}")


def ejemplificar_diccionarios():
    # 2. DICCIONARIOS (Pares Clave-Valor, Mutables)
    # Útiles para mapear identidades (ej: base de datos simple).
    estudiante = {
        "Nombre": "Juan",
        "Edad": 21,
        "Carrera": "Ingeniería"
    }
    estudiante["Nota"] = 4.5 # Agregar nueva clave
    print(f"\n[DICCIONARIO]: {estudiante}")
    print(f"Nombre del estudiante: {estudiante['Nombre']}")


def ejemplificar_tuplas():
    # 3. TUPLAS (Inmutables, Ordenadas)
    # Útiles para datos que NO deben cambiar nunca (ej: coordenadas).
    coordenadas = (10, 20)
    print(f"\n[TUPLA]: {coordenadas}")
    # coordenadas[0] = 5  <-- ¡Esto daría error! Las tuplas no se pueden cambiar.


def ejemplificar_sets():
    # 4. CONJUNTOS (Sin duplicados, Desordenados)
    # Útiles para operaciones matemáticas de conjuntos o eliminar duplicados.
    numeros = {1, 2, 2, 3, 4, 4, 5}
    print(f"\n[SET (Sin duplicados)]: {numeros}")


if __name__ == "__main__":
    print("--- APRENDIENDO ESTRUCTURAS DE DATOS EN PYTHON ---")
    ejemplificar_listas()
    ejemplificar_diccionarios()
    ejemplificar_tuplas()
    ejemplificar_sets()
