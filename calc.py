# -*- coding: utf-8 -*-
from __future__ import division
import math
import string


def okrug2(num, depth=2):
    # Округление числа до двух знаком после запятой
    # Результат – число типа float
    return float(u"%.2f" % num)
    # return int(num * 10 ** depth + 0.5) / 10 ** depth


def rub_comma(dot_num, new_format=False):
    """ Замена десятичной точки на запятую.
     
    Замена десятичной точки на запятую с добавлением сокращения «руб.»    
    Если new_format=True, добавляется знак ₽ вместо «руб.»
    """
    if new_format:
        return u"{0}₽".format(string.replace(u"%.2f" % dot_num, ".", ","))
    else:
        return u"{0} руб.".format(string.replace(u"%.2f" % dot_num, ".", ","))


e = okrug2(math.e)
rub = rub_comma(math.pi)

x = 14 / 3

print rub
print rub_comma(500 / 25, True)
print rub_comma(2 * okrug2(x))
print "{0}%".format((okrug2(x) - x) / okrug2(x) * 100)
