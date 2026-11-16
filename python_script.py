import os

def print_hola_mundo():
    nombre = os.getenv("USERNAME")
    print(f"Hola Mundo, hola {nombre}")
    
if __name__ == "__main__":
    print_hola_mundo()

