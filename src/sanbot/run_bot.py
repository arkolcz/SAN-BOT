import sys
from sanbot.bot import Bot
from sanbot.utils import get_from_dotenv
from sanbot.constants import BOT_TOKEN_DOTENV_KEY


def main() -> int:
    token = get_from_dotenv(BOT_TOKEN_DOTENV_KEY)
    bot = Bot()
    bot.run(token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
