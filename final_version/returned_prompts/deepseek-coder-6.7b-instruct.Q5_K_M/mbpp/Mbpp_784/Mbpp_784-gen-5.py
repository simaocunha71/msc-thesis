
def mul_even_odd(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return evens[0]*odds[0]

print(mul_even_odd([1,3,5,7,4,1,6,8])) # Expected output: 4





