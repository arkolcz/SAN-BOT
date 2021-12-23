from sanbot import run_bot
from mock import patch


@patch("sanbot.run_bot.Bot")
@patch("sanbot.run_bot.get_from_dotenv")
def test_main(mock_get_from_dotenv, _):
    mock_get_from_dotenv.return_value = None

    result = run_bot.main()

    assert result == 0
