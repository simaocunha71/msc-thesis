def mul_even_odd(lst):
    evens, odds = [], []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) == 0:
        return "No even number in the list"
    if len(odds) == 0:
        return "No odd number in the list"
    return evens[0] * odds[0]








# assert mul_even_odd([1,3,5,7,4,1,6,8])==4
# print(mul_even_odd([1,3,5,7,4,1,6,8]))
# print(mul_even_odd([1,3,5,7,4,1,6]))
# print(mul_even_odd([1,3,5,7,4]))
# print(mul_even_odd([1,3,5,7]))
# print(mul_even_odd([1,3,5]))
# print(mul_even_odd([1]))
# print(mul_even_odd([]))






















"""
def mul_even_odd(lst):
    evens, odds = [], []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) == 0:
        return "No even number in the list"
    if len(odds) == 0:
        return "No odd number in the list"
    return evens[0] * odds[0]
"""
"""
def mul_even_odd(lst):
    evens, odds = [], []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) == 0:
        return "No even number in the list"
    if len(