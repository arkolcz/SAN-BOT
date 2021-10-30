import sys
from bot import Bot
from utils import get_from_dotenv
from constants import BOT_TOKEN_DOTENV_KEY


def main() -> int:
    token = get_from_dotenv(BOT_TOKEN_DOTENV_KEY)
    bot = Bot()
    bot.run(token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
