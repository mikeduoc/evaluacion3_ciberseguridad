import json
from pathlib import Path


def load_data(file_name, base_dir="data"):
    base_path = Path(base_dir).resolve()
    target_path = (base_path / file_name).resolve()

    try:
        target_path.relative_to(base_path)
    except ValueError:
        raise ValueError("Ruta no permitida")

    if target_path.suffix != ".json":
        raise ValueError("Solo se permiten archivos JSON")

    with open(target_path, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    file_name = input("Enter JSON file name: ")
    data = load_data(file_name)
    print(data)