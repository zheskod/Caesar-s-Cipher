# Функция для шифровки/дешифровки на английском языке
def eng_code(change, text, step):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = []
    if change == 'ш':
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].isupper():
                    new_text.append(eng_upper_alphabet[(eng_upper_alphabet.find(text[i]) + step) % 26])
                elif text[i].islower():
                    new_text.append(eng_lower_alphabet[(eng_lower_alphabet.find(text[i]) + step) % 26])
            else:
                new_text.append(text[i])
    elif change == 'д':
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].isupper():
                    new_text.append(eng_upper_alphabet[(eng_upper_alphabet.find(text[i]) - step) % 26])
                elif text[i].islower():
                    new_text.append(eng_lower_alphabet[(eng_lower_alphabet.find(text[i]) - step) % 26])
            else:
                new_text.append(text[i])
    print(*new_text, sep='')
    return

# Функция для шифровки/дешифровки на русском языке
def ru_code(change, text, step):
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    new_text = []
    if change == 'ш':
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].isupper():
                    new_text.append(rus_upper_alphabet[(rus_upper_alphabet.find(text[i]) + step) % 32])
                elif text[i].islower():
                    new_text.append(rus_lower_alphabet[(rus_lower_alphabet.find(text[i]) + step) % 32])
            else:
                new_text.append(text[i])
    elif change == 'д':
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].isupper():
                    new_text.append(rus_upper_alphabet[(rus_upper_alphabet.find(text[i]) - step) % 32])
                elif text[i].islower():
                    new_text.append(rus_lower_alphabet[(rus_lower_alphabet.find(text[i]) - step) % 32])
            else:
                new_text.append(text[i])
    print(*new_text, sep='')
    return


# приветствие
print("Caesar's Cipher v.1.0. приветствует тебя!")

# вопрос 1
change_encryption = 0
while change_encryption != 'д' and change_encryption != 'ш':
    change_encryption = input('Будем шифровать (ш) или дешифровать (д) ?: ')

# выбор языка
text_main = 0
while text_main != 'а' and text_main != 'р':
    text_main = input('На каком языке будем шфировать, английский (а) или русский (р)?: ')

# текст шифровки/расшифровки
code_txt = input('Введите текст: ')

choice_step = 0
while choice_step != 'да' and choice_step != 'нет':
    choice_step = input('Известен ключ (шаг сдвига)? (да/нет): ')
    if choice_step == 'да':
        shift_step = int(input('Введите (шаг сдвига): '))
        if text_main == 'р':
            ru_code(change_encryption, code_txt, shift_step)
        else:
            eng_code(change_encryption, code_txt, shift_step)

    if choice_step == 'нет':
        shift_step = int(input('Введите количество попыток: '))
        for j in range(0, shift_step+1):
            shift_step = j
            if text_main == 'р':
                ru_code(change_encryption, code_txt, shift_step)
            else:
                eng_code(change_encryption, code_txt, shift_step)
