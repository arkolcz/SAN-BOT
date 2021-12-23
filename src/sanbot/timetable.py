from typing import Any, Union
from urllib.error import HTTPError
import mechanize  # type: ignore
from sanbot.utils import get_from_dotenv
from sanbot.constants import (
    SAN_SITE_URL,
    SAN_LOGIN_DOTENV_KEY,
    SAN_PASS_DOTENV_KEY,
    SAN_SITE_LOGIN_KEYWORD,
    SAN_SITE_PASSWORD_KEYWORD,
    SAN_SITE_LOGIN_FORM_IDX,
    SAN_CLASS_SCHEDULE_REGEX,
)
import re


class Timetable:
    __slots__ = "login", "password", "actual_timetable"

    def __init__(self) -> None:
        self.login = get_from_dotenv(SAN_LOGIN_DOTENV_KEY)
        self.password = get_from_dotenv(SAN_PASS_DOTENV_KEY)
        self.actual_timetable = ""

    def get_san_timetable(self) -> str:
        return self.actual_timetable

    def check_timetable_changes(self) -> bool:
        timetable = self._get_current_timetable_from_site()
        if timetable and timetable != self.actual_timetable:
            self.actual_timetable = timetable
            print("Synced new Timetable!")
            return True
        return False

    def _get_current_timetable_from_site(self) -> Union[str, Any]:
        # TODO: This could be potentially optimized. Instead of creating a new
        # browser object each time, existing object could be reused.
        browser = mechanize.Browser()
        try:
            browser.open(SAN_SITE_URL)
            browser.select_form(nr=SAN_SITE_LOGIN_FORM_IDX)
            browser.form[SAN_SITE_LOGIN_KEYWORD] = self.login
            browser.form[SAN_SITE_PASSWORD_KEYWORD] = self.password
            response = browser.submit()
            response = str(response.read())
            match = re.search(SAN_CLASS_SCHEDULE_REGEX, response)

            if match:
                return match.group(0)
            return None
        except HTTPError:
            print(f"Service {SAN_SITE_URL} is unavaiable")
            return None
