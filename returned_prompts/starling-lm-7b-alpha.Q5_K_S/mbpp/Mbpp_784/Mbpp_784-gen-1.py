"""
def mul_even_odd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) == 0:
        return 0
    if len(even) == 0:
        return odd[0]
    return even[0] * odd[0]

assert(mul_even_odd([1,3,5,7,4,1,6,8]) == 4)
"""

def mul_even_odd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) == 0:
        return 0
    if len(even) == 0:
        return odd[0]
    return even[0] * odd[0]

assert(mul_even_odd([1,3,5,7,4,1,6,8]) == 4)




def mul_even_odd(l):
    if len(l) < 2:
        return 0
    else:
        evens = [x for x in l if x % 2 == 0]
        odds = [x for x in l if x % 2 != 0]
        if len(evens) == 0:
            return odds[0]
        elif len(odds) == 0:
            return evens[0]
        else:
            return evens[0] * odds[0]

assert(mul_even_odd([1,3,5,7,4,1,6,8]) == 4)


def mul_even_odd(l):
    evens = []
    odds = []
    for i in l:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(odds) == 0:
        return 0
   