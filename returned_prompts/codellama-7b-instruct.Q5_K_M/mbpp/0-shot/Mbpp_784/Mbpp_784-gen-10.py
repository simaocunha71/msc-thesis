"""
def mul_even_odd(my_list):
    my_list = [int(x) for x in my_list]
    even = []
    odd = []
    for i in my_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even[0] * odd[0]
"""
