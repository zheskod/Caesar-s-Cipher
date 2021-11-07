from random import *

def eng_code(text, step):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ru_code(text, step):
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# приветствие
print("Caesar 's Cipher v.1.0. приветствует тебя!")

# вопрос 1
input('Будем шифровать (ш) или дешифровать (д) ?: ')

# выбор языка
input('На каком языке будем шфировать, английский (а) или русский (р)?: ')

# шаг сдвига
shift_step = int(input('Ключ? (шаг сдвига): '))
