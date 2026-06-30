import subprocess


ALLOWED_COMMANDS = {
    "whoami": ["whoami"],
    "hostname": ["hostname"]
}


def run_command(command_name):
    if command_name not in ALLOWED_COMMANDS:
        raise ValueError("Comando no permitido")

    result = subprocess.run(
        ALLOWED_COMMANDS[command_name],
        capture_output=True,
        text=True,
        check=True,
        shell=False,
        timeout=5
    )

    return result.stdout.strip()


if __name__ == "__main__":
    command = input("Enter allowed command [whoami/hostname]: ")
    output = run_command(command)
    print(output)