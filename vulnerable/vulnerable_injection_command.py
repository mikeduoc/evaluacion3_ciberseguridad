
import os

def run_command(command):
    # VULNERABILIDAD: La entrada del usuario se inserta directamente en el comando del sistema
    os.system(command)

user_command = input("Enter a command: ")
run_command(user_command)
