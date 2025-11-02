# Test1.py
# Archivo de prueba con múltiples patrones vulnerables para que CodeQL los detecte.
# NOTA: Las funciones vulnerables NO se llaman en __main__, así no realizan acciones peligrosas.

import sqlite3
import subprocess
import pickle
import base64

# -------------------------
# 1) SQL Injection (vulnerable)
# -------------------------
def vuln_sql_injection(user):
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE IF NOT EXISTS users(username TEXT);")
    # Vulnerabilidad: concatenación directa de input en la query
    query = "SELECT * FROM users WHERE username = '" + user + "';"
    # CodeQL detecta el flujo de datos hacia la consulta SQL
    return conn.execute(query).fetchall()


# -------------------------
# 2) Eval inseguro
# -------------------------
def vuln_eval(user_code):
    # Vulnerabilidad: eval sobre input arbitrario
    # Si se llamara con input del usuario, permitiría ejecución arbitraria
    return eval(user_code)


# -------------------------
# 3) Command Injection (shell=True)
# -------------------------
def vuln_cmd_injection(user_cmd):
    # Vulnerabilidad: construcción de comando con input y uso de shell=True
    cmd = f"echo {user_cmd}"   # echo es inocuo, pero el patrón (concatenación + shell=True) es lo que CodeQL detecta
    subprocess.run(cmd, shell=True)


# -------------------------
# 4) Deserialización insegura con pickle
# -------------------------
def vuln_pickle(b64):
    # Vulnerabilidad: deserializar datos no confiables con pickle.loads
    raw = base64.b64decode(b64)
    return pickle.loads(raw)


# -------------------------
# 5) Secret hardcodeado
# -------------------------
API_KEY = "AKIA_THIS_IS_A_TEST_SECRET_1234567890"  # Hard-coded secret (CodeQL/Secret Scanning)
DB_PASSWORD = "Passw0rd!"

# -------------------------
# No ejecutar nada peligroso en main
# -------------------------
if __name__ == "__main__":
    print("Test file with vulnerable patterns for CodeQL.")
    print("The functions are defined but NOT called, so running this file is safe.")
    # Si quieres probar ejecución local segura, descomenta y usa valores controlados (NO recomendado en entornos públicos).
    # Ej:
    # print(vuln_sql_injection("admin"))
    # print(vuln_eval("1+1"))
