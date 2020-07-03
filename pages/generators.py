import random
import string
import datetime
import re


def generate_id():
    num1 = str(random.randint(7000000, 7999999))
    num2 = str(random.randint(111, 999))
    number = ''.join([num1, random.choice('A'), num2, 'PB'])
    weights = [7, 3, 1] * 6
    checksum = 0
    for ch, w in zip(number, weights):
        def get_value(_ch):
            if not _ch in string.ascii_uppercase:
                return int(_ch)
            else:
                return string.ascii_uppercase.index(_ch) + 10
        checksum += get_value(ch) * w
    checksum %= 10
    number += str(checksum)
    return number


def randomStringLatin(stringLength=8):
    return "".join(random.choice(string.ascii_lowercase) for i in range(stringLength))


def randomStringCirillic(stringLength=8):
    letters = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
    return "".join(random.choice(letters) for i in range(stringLength))


def randomDigits(stringLength=8):
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(stringLength))


def generate_username():
    d = datetime.datetime.now()
    d = d.strftime('%y%m%d%H%M')
    return d

# print(bool(re.match(r'[1-7]\d{6}[ABCHKEM]\d{3}(PB|BA|BI)\d', '3344223B555BIb')))
# print(bool(re.match(r'\d{7}[A-H]\d{3}(PB|BA|BI)', '3344223D555Bw')))
# print(number[-1:])
