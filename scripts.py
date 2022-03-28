""  # Temporary workaround until Poetry supports scripts
# https://github.com/sdispater/poetry/issues/241.
from subprocess import check_call


module_id = "notebooks"
project_id = "notebooks"
project = "c-core-labs"


def start() -> None:
    check_call(["jupyter", "lab"])


def freeze() -> None:
    with open("requirements.txt", "w") as file:
        check_call(
            ["poetry", "export", "-f", "requirements.txt", "--without-hashes"],
            stdout=file,
        )
