import random
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

#функции проверок вводимых пользователем данных
def is_valid_num(text):
    if text.isdigit() and int(text) > 0:
        return True
    print('Необходимо ввести положительное число, попробуйте еще раз: ', end='')
    return False

def is_bool(text):
    if text.lower() == 'д' or text.lower() == 'н':
        return True
    else:
        print('Необходимо ввести "д" или "н", попробуйте ещё раз: ', end='')
        return False

#Ввод данных от пользователя
clarification = '("д" = да, "н" = нет): '

print('Сколько паролей необходимо сгенерировать?: ', end='')
count = input()
while not is_valid_num(count):
    count = input()

print('Какая длина пароля необходима?: ', end='')
length = input()
while not is_valid_num(length):
    length = input()

print(f'Включать цифры в пароль? {clarification}', end='')
num = input()
while not is_bool(num):
    num = input()

print(f'Включать заглавные буквы? {clarification}', end='')
upp = input()
while not is_bool(upp):
    upp = input()

print(f'Включать буквы в нижнем регистре? {clarification}', end='')
low = input()
while not is_bool(low):
    low = input()

print(f'Включать пунктуацию? {clarification}', end='')
pun = input()
while not is_bool(pun):
    pun = input()

print(f'Исключать неоднозначные символы(il1Lo0O)? {clarification}', end='')
exceptions = input()
while not is_bool(exceptions):
    exceptions = input()

#формируем строку допустимых символов
if num.lower() == 'д':
    chars += DIGITS
if upp.lower() == 'д':
    chars += LOWERCASE_LETTERS
if low.lower() == 'д':
    chars += UPPERCASE_LETTERS
if pun.lower() == 'д':
    chars += PUNCTUATION
if exceptions.lower() == 'д':
    chars = chars.replace('i', '')
    chars = chars.replace('l', '')
    chars = chars.replace('1', '')
    chars = chars.replace('L', '')
    chars = chars.replace('o', '')
    chars = chars.replace('0', '')
    chars = chars.replace('O', '')

#функция создания пароля
def generate_password(length, chars):
    if len(chars) >= int(length):
        print(''.join(random.sample(chars, int(length))))
    elif len(chars) != 0:
        print(''.join(random.sample(chars, len(chars)) + [random.choice(chars) for _ in range(int(length) - len(chars))]))
    else:
        print('Нет символов для генерации вашего пароля!')

# генерация необходимого кол-ва паролей
for _ in range(int(count)):
    generate_password(length, chars)