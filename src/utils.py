import os
from typing import Any, Union
from dotenv import load_dotenv  # type: ignore


def get_from_dotenv(key: str) -> Union[str, Any]:
    load_dotenv()
    return os.environ.get(key)
