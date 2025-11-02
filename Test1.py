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

print("Generar alerta en CodeQL")

# sql_injection.py
import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    # 🚨 Vulnerable: concatenación directa del input en la consulta
    query = "SELECT * FROM users WHERE username = '%s';" % username
    cur = conn.execute(query)
    return cur.fetchall()

if __name__ == "__main__":
    u = input("username: ")
    print(get_user(u))

# cmd_injection.py
import subprocess

def list_user_files(user):
    # 🚨 Vulnerable: shell=True con entrada directa del usuario
    cmd = f"ls -la /home/{user}"
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    u = input("user: ")
    list_user_files(u)


import sqlite3

def get_user_info():
    conn = sqlite3.connect("users.db")
    username = input("Enter username: ")
    # 🚨 Vulnerabilidad: concatenar directamente el input del usuario
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    result = conn.execute(query)
    for row in result:
        print(row)

get_user_info()
