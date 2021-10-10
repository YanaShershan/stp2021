from colorama import init
from colorama import Fore, Back, Style
init()

print( Fore.BLACK)
print( Back.BLUE )
what = input("Что делаем? (+,-): " )
print( Back.GREEN )
a = float( input("Введи первое число: ") )
b = float( input("Введи второе число: ") )
print( Back.CYAN )
if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
else:
    print("Выбрана неверная операция!")
    input()