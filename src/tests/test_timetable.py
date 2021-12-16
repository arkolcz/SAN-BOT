from bot.timetable import Timetable
from mock import patch
import pytest


def mock_init(self, login="", password="", actual_timetable=""):
    self.login = login
    self.password = password
    self.actual_timetable = actual_timetable


@patch("bot.timetable.get_from_dotenv")
def test_init_timetable(mock_get_from_dotenv):
    mock_get_from_dotenv.return_value = "dummy"
    expected_result = ("dummy", "dummy", "")

    obj = Timetable()
    result = (obj.login, obj.password, obj.actual_timetable)

    assert expected_result == result


@patch.object(Timetable, "__init__", mock_init)
def test_get_san_timetable():
    expected_result = "dummy_timetable"

    obj = Timetable(actual_timetable=expected_result)
    result = obj.get_san_timetable()

    assert expected_result == result


@pytest.mark.parametrize(
    "timetable_output, actual_timetable, expected_result",
    [
        ("dummy_timetable", "", True),
        ("dummy_timetable", "dummy_timetable", False),
        ("", "dummy_timetable", False),
        ("", "", False),
    ],
)
@patch.object(Timetable, "__init__", mock_init)
@patch.object(Timetable, "_get_current_timetable_from_site")
def test_check_timetable_changes(
    mock_get_current_timetable_from_site,
    timetable_output,
    actual_timetable,
    expected_result,
):
    mock_get_current_timetable_from_site.return_value = timetable_output
    obj = Timetable(actual_timetable=actual_timetable)
    result = obj.check_timetable_changes()
    assert expected_result == result


@pytest.mark.parametrize(
    "response, expected_result",
    [
        (
            "https://lodz.san.edu.pl/wgrane-pliki/iii-inf-z-0000.pdf",
            "https://lodz.san.edu.pl/wgrane-pliki/iii-inf-z-0000.pdf",
        ),
        (
            "dummyhttps://lodz.san.edu.pl/wgrane-pliki/iii-inf-z-2.zip",
            "https://lodz.san.edu.pl/wgrane-pliki/iii-inf-z-2.zip",
        ),
        ("https://invalid_link.pdf", None),
        ("", None),
    ],
)
@patch.object(Timetable, "__init__", mock_init)
@patch("bot.timetable.mechanize.Browser")
def test_get_current_timetable_from_site(mock_browser, response, expected_result):
    mock_browser().submit().read.return_value = response

    obj = Timetable()
    result = obj._get_current_timetable_from_site()

    assert expected_result == result
