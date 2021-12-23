from sanbot.constants import BOT_TOKEN_DOTENV_KEY
from sanbot.utils import get_from_dotenv
import pytest


def test_get_from_dotenv_success(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "DUMMY_TOKEN")
    assert get_from_dotenv(BOT_TOKEN_DOTENV_KEY) == "DUMMY_TOKEN"


def test_get_from_dotenv_fail():
    KEY = "NON_EXISTENT_KEY"
    with pytest.raises(OSError):
        _ = get_from_dotenv(KEY)
