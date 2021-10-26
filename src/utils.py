import os
from typing import Optional
from dotenv import load_dotenv


def get_from_dotenv(key: str) -> Optional[str]:
    load_dotenv()
    return os.environ.get(key)
