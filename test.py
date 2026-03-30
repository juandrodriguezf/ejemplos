import sys
import platform

def main():
    print("¡Hola! Este es un programa de prueba en Python.")
    print("-" * 40)
    print(f"Sistema Operativo: {platform.system()} {platform.release()}")
    print(f"Versión de Python: {sys.version}")
    print("-" * 40)
    
    nombre = input("¿Cómo te llamas? ")
    print(f"¡Mucho gusto, {nombre}! El entorno de Python en tu IDE parece estar funcionando correctamente.")

if __name__ == "__main__":
    main()
