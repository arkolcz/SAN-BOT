import mechanize
from utils import get_from_dotenv
from constants import (SAN_LOGIN_DOTENV_KEY, SAN_PASS_DOTENV_KEY, SAN_SITE_LOGIN_KEYWORD, SAN_SITE_PASSWORD_KEYWORD,
                       SAN_SITE_LOGIN_FORM_IDX, SAN_CLASS_SCHEDULE_REGEX)
import re


class Crawler():
    __slots__ = 'page', 'login', 'password'

    def __init__(self, page) -> None:
        self.page = page
        self.login =  ''
        self.password = ''


    def get_schedule(self):
        try:
            self._get_user_credentials()
        except:
            print('No SAN credentials in .env conf')
            # TODO: Add propper logging and error handling

        browser = mechanize.Browser()
        browser.open(self.page)
        browser.select_form(nr=SAN_SITE_LOGIN_FORM_IDX)
        browser.form[SAN_SITE_LOGIN_KEYWORD] = self.login
        browser.form[SAN_SITE_PASSWORD_KEYWORD] = self.password
        response = browser.submit()
        response = str(response.read())
        match = re.search(SAN_CLASS_SCHEDULE_REGEX, response)

        if match:
            return match.group(0)


    def _get_user_credentials(self) -> None:
        self.login = get_from_dotenv(SAN_LOGIN_DOTENV_KEY)
        self.password = get_from_dotenv(SAN_PASS_DOTENV_KEY)

