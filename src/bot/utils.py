import os
from typing import Any, Union
from dotenv import load_dotenv


def get_from_dotenv(key: str) -> Union[str, Any]:
    load_dotenv()
    value = os.environ.get(key)
    if value is None:
        raise OSError(f"No value found for key {key} in .env variables")
    return value
