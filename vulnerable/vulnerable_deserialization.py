
import pickle

def load_data(file_path):
    # VULNERABILIDAD: Deserialización de datos sin validar, permitiendo ejecución de código arbitrario
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

file_path = input("Enter the path to the data file: ")
data = load_data(file_path)
print(data)
