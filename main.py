# Функция для шфировки/дешифровки на английском языке
def eng_code(change, text, step):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                new_text.append(eng_upper_alphabet[(eng_upper_alphabet.find(text[i]) + step) % 26])
            elif text[i].islower():
                new_text.append(eng_lower_alphabet[(eng_lower_alphabet.find(text[i]) + step) % 26])
        else:
            new_text.append(text[i])
    print(*new_text, sep='')
    return

# Функция для шфировки/дешифровки на русском языке
def ru_code(change, text, step):
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    new_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                new_text.append(rus_upper_alphabet[(rus_upper_alphabet.find(text[i]) + step) % 32])
            elif text[i].islower():
                new_text.append(rus_lower_alphabet[(rus_lower_alphabet.find(text[i]) + step) % 32])
        else:
            new_text.append(text[i])
    print(*new_text, sep='')
    return


# приветствие
print("Caesar's Cipher v.1.0. приветствует тебя!")

# вопрос 1
change_encryption = input('Будем шифровать (ш) или дешифровать (д) ?: ')

# выбор языка
text_main = input('На каком языке будем шфировать, английский (а) или русский (р)?: ')

# шаг сдвига
shift_step = int(input('Ключ? (шаг сдвига): '))

# текст шифровки/расшифровки
code_txt = input('Введите текст: ')

if text_main == 'р':
    ru_code(change_encryption, code_txt, shift_step)
else:
    eng_code(change_encryption, code_txt, shift_step)
