# Archivo: Test1.py
# Contiene varios patrones de vulnerabilidad para CodeQL
# NO ejecutar en producción

import os
import pickle
import sqlite3

def vulnerable_sql(user_input):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # Vulnerabilidad SQL Injection
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_command(user_input):
    # Vulnerabilidad: Command Injection
    os.system(f"ping {user_input}")

def vulnerable_pickle(data):
    # Vulnerabilidad: Deserialización insegura
    obj = pickle.loads(data)
    return obj

def main():
    # No ejecuta nada peligroso directamente
    print("Archivo con vulnerabilidades para análisis de CodeQL.")

if __name__ == "__main__":
    main()

print("Forzando el sarif ")