from sanbot.bot import Bot
from mock import patch


@patch('sanbot.bot.discord.Client.__init__')
@patch('sanbot.bot.Timetable')
def test_bot_init(mock_timetable, mock_discord_client_init):
    mock_discord_client_init.return_value = None
    mock_timetable.return_value = 'dummy_obj'

    obj = Bot()
    assert obj.timetable == 'dummy_obj'
    assert obj.channel == None