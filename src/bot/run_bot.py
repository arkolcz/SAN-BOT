import sys
from bot.bot import Bot
from bot.utils import get_from_dotenv
from bot.constants import BOT_TOKEN_DOTENV_KEY


def main() -> int:
    token = get_from_dotenv(BOT_TOKEN_DOTENV_KEY)
    bot = Bot()
    bot.run(token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
