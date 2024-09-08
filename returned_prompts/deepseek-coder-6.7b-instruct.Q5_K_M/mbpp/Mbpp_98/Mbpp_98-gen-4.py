
def multiply_num(lst):
    mult = 1
    for num in lst:
        mult *= num
    return mult / len(lst)

assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)

"""
In the function, we first initialize a variable mult to 1, which will be used to hold the product of all numbers in the list. Then we loop over each number in the list, multiplying the current number with mult. Finally, we divide the product by the length of the list to get the average and return it.
"""

#2

