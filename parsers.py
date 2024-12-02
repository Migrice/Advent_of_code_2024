from pathlib import Path

BASE_DIR = Path(__name__).parent


def read_file(path: str):
    workdir = BASE_DIR / path

    with open(workdir, "r") as file:
        return file.read().splitlines()
