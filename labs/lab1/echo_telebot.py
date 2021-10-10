from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import config
from pyowm.utils import timestamps
import telebot

config_dict = get_default_config()
owm = OWM('156794c6821bacc9dbcb52952af077bb', config_dict)
config_dict['language'] = 'ru'
bot = telebot.TeleBot("2072774485:AAGuP3rnvjtfKjY2jtozvd_eW_0b__dnkis")

@bot.message_handler(content_types =['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    status = w.detailed_status
    #bot.reply_to(message, message.text)

    answer = "В городе " + message.text + " сейчас " + status + "\n"
    answer += "Температура сейчас " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Советую закутаться во все возможное!"
    elif temp < 20:
        answer += "Стоит задуматься на выбором одежды потеплее "
    else:
        answer += "Не смотри на людей, надевай что угодно"       
    
    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )