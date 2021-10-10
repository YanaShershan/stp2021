from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import config
from pyowm.utils import timestamps

config_dict = get_default_config()
place = input("В каком городе вы хотите узнать погоду? ")
owm = OWM('156794c6821bacc9dbcb52952af077bb', config_dict)
config_dict['language'] = 'ru'
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]
status = w.detailed_status
print( "В городе " + place + "сейчас " + status)
print( "Температура сейчас " + str(temp))

if temp < 10:
    print( "Советую закутаться во все возможное!")
elif temp < 20:
    print( "Стоит задуматься на выбором одежды потеплее ")
else:
    print( "Не смотри на людей, надевай что угодно")       