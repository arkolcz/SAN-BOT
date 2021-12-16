from src import utils
from src.constants import BOT_TOKEN_DOTENV_KEY
import pytest


def test_get_from_dotenv_success(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "DUMMY_TOKEN")
    assert utils.get_from_dotenv(BOT_TOKEN_DOTENV_KEY) == "DUMMY_TOKEN"


def test_get_from_dotenv_fail():
    KEY = "NON_EXISTENT_KEY"
    with pytest.raises(OSError):
        _ = utils.get_from_dotenv(KEY)
