import random
from secrets import choice
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

#Ввод данных от пользователя
clarification = '("д" = да, "н" = нет): '
count = int(input('Сколько паролей необходимо сгенерировать?: '))
length = int(input('Какая длина пароля необходима?: '))
num = input(f'Включать цифры в пароль? {clarification}')
upp = input(f'Включать заглавные буквы? {clarification}')
low = input(f'Включать буквы в нижнем регистре? {clarification}')
pun = input(f'Включать пунктуацию? {clarification}')
exceptions = input(f'Исключать неоднозначные символы(il1Lo0O)? {clarification}')

if num == 'д':
    chars += DIGITS
if upp == 'д':
    chars += LOWERCASE_LETTERS
if low == 'д':
    chars += UPPERCASE_LETTERS
if pun == 'д':
    chars += PUNCTUATION
if exceptions == 'д':
    chars = chars.replace('i', '')
    chars = chars.replace('l', '')
    chars = chars.replace('1', '')
    chars = chars.replace('L', '')
    chars = chars.replace('o', '')
    chars = chars.replace('0', '')
    chars = chars.replace('O', '')

def generate_password(length, chars):
    if len(chars) >= length:
        print(''.join(random.sample(chars, length)))
    elif len(chars) != 0:
        print(''.join(random.sample(chars, len(chars)) + [random.choice(chars) for _ in range(length - len(chars))]))
    else:
        print('Нет символов для генерации вашего пароля!')

for _ in range(count):
    generate_password(length, chars)