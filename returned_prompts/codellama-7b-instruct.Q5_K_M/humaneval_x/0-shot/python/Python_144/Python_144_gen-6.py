
import re


def simplify(x, n):
    x_num, x_den = map(int, re.findall(r'\d+', x)[::-1])
    n_num, n_den = map(int, re.findall(r'\d+', n)[::-1])
    if x_num * n_den == x_den * n_num:
        return True
    else:
        return False


assert simplify('1/5', '5/1') == True
assert simplify('1/6', '2/1') == False
assert simplify('7/10', '10/2') == False
