from pathlib import Path
from typing import Union

def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent.parent.resolve()


def get_src_path() -> Path:
    """Returns Path of the src/ folder."""
    return get_project_root().joinpath("src")


def get_relative_path(path: Union[str, Path]) -> Path:
    """Returns Path relative to src/ folder."""
    try:
        return Path(path).resolve().relative_to(get_src_path())
    except:
        return path
