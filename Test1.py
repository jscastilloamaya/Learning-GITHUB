print("Hola Git")

print("Desarrollo rama2")
rama4=4
print("Desarrollo rama4")
print("Hola Git segundo commit")

print("Hola Git cambio trucho")

print("Cambio")

print("11:12 am")
print("11:20 am")
print("9-08-2025")

print("El cambio Rescatame ")
print("Rama Principal")
print("Desarrollo de main")
print("Rama de desarrollo")
print("Desarrollo 1")
print("Rama 1")

print("Rama 3 Pro mega cambiada")
rama3=3

# file: vulnerable.py

import os

def delete_user_file(username):
    # 🚨 Vulnerabilidad: el input del usuario se usa directamente en un comando del sistema
    command = f"rm -rf /home/{username}/data"
    os.system(command)

# Simulamos entrada del usuario
user_input = input("Enter your username: ")
delete_user_file(user_input)
