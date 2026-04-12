def add(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b

def multiply(a, b):
    """Multiplica dos números y retorna el resultado."""
    return a * b

def subtract(a, b):
    """Resta dos números y retorna el resultado."""
    return a - b

if __name__ == "__main__":
    print("Calculadora Iniciada")
    
    try:
        x = float(input("Ingrese el primer número: "))
        y = float(input("Ingrese el segundo número: "))
        
        resultado = multiply(x, y)
        print(f"La multiplicación de {x} * {y} es: {resultado}")
        
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
