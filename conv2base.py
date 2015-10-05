# -*- coding:utf-8 -*-
import math
import sys

sys.setrecursionlimit(10000)
limit = 0
alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class ShortBaseException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = int(value)


def get_numb_for_rec(a, b):
    mod = []
    l = -1

    while len(mod) < 10000:
        m = a % b
        if m == 0:
            break
        if m in mod:
            l = mod.index(m)
            break
        else:
            mod.append(m)
            a = m * 10
    return l


def fractionToDecimal(a, b):
    if a * b < 0:
        pos = False
    else:
        pos = True
    a = abs(a)
    b = abs(b)

    maxlen = 10000

    if a == 0 or b == 0:
        return "0"

    mod = []
    res = []
    l = -1
    while len(mod) < maxlen:
        res.append(a / b)
        m = a % b
        if m == 0:
            break
        if m in mod:
            l = mod.index(m)
            break
        else:
            mod.append(m)
            a = m * 10

    if len(res) == 1:
        s = str(res[0])
    else:
        s = str(res[0]) + "."
        if l == -1:
            s = s + "".join([str(n) for n in res[1::]])
        else:
            s = s + "".join([str(n) for n in res[1:l + 1]]) + "(" + "".join([str(n) for n in res[l + 1::]]) + ")"
    if pos:
        return s
    else:
        return "-" + s


def number_int_to_base(c, k, newc):
    newc.append(c % k)
    dig = c / k

    if (int(dig) == 0):
        return

    number_int_to_base(dig, k, newc)


def number_fract_to_base(c, k, newc_d):
    global limit
    limit += 1

    res = c * k
    newc_d.append(int(math.modf(res)[1]))

    if math.modf(res)[0] == 0.0:
        return

    while limit < sys.getrecursionlimit() - 3:
        number_fract_to_base(math.modf(res)[0], k, newc_d)


def number_to_other_base(a, b, k):
    global limit
    limit = 0

    if k < 2 or k > 36:
        raise ShortBaseException(k)

    l = get_numb_for_rec(a, b)

    if k == 10:
        return fractionToDecimal(int(a), int(b))
    else:
        a = float(a)

    c = a / b
    newc = []
    newc_d = []
    str_answ = ''
    minus = ''

    if c < 0:
        minus = '-'
    c = abs(c)

    if math.modf(c)[1] != 0.0:
        if math.modf(c / k)[1] == 0.0:
            str_answ = alphabet[int(math.modf(c)[1])]
        else:
            number_int_to_base(c, k, newc)
            answ = [int(i) for i in reversed(newc)]
            for key, i in enumerate(answ):
                if alphabet[i]:
                    answ[key] = alphabet[i]
            str_answ = ''.join(map(str, answ))
    else:
        str_answ = '0'

    if math.modf(c)[0] != 0.0:
        number_fract_to_base(math.modf(c)[0], k, newc_d)
        only = 1
        first = True
        key_only = -1
        for key, i in enumerate(newc_d):
            if key < len(newc_d) - 1:
                if int(newc_d[key]) == int(newc_d[key + 1]):
                    if first:
                        key_only = key
                        first = False
                    only = only * 1
                else:
                    only = only * 0
            if alphabet[i]:
                newc_d[key] = alphabet[i]
        if only and key_only != -1:
            return minus + str_answ + '.' + "".join([str(n) \
                                                     for n in newc_d[0:key_only]]) + "(" + "".join([str(n) \
                                                                                                    for n in newc_d[
                                                                                                             key_only:key_only + 1]]) + ")"
        str_answ = str_answ + '.'
        if l == -1:
            str_answ = str_answ + ''.join(map(str, newc_d))
        else:
            str_answ = str_answ + "".join([str(n) for n in newc_d[0:l]]) \
                       + "(" + "".join([str(n) for n in newc_d[l::]]) + ")"

    str_answ = minus + str_answ

    return str_answ


def main():
    print u"Данная программа для расчета частного от деления двух чисел," \
          u" переведенного в систему счисления(СС).\n" \
          u"СС пользователь задает сам. Допустимое значение основания для СС" \
          u" от 2 до 36.\n"
    x = 0
    while x == 0:
        print u"Введите делимое, делитель и основание для новой системы" \
              u" счисления через пробел:"
        try:
            pair = raw_input()

            pair = pair.split(" ")[0:3]
            pair = [float(i) for i in pair]

            c = pair[0] / pair[1]

            res = number_to_other_base(pair[0], pair[1], pair[2])
            print u'Результат:'
            print res

            x = 1
        except ValueError:
            print u"Необходимо ввести числа."
            pass
        except IndexError:
            print u"Недостаточно параметров."
            pass
        except ZeroDivisionError:
            print u"Делитель не должен быть равен нулю."
            pass
        except ShortBaseException as ex:
            print u"Основание для системы счисления должно быть от 2 до 36." \
                  u" А введено {0}.".format(ex.value)
            pass


main()
