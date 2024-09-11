def is_polite(num):
    if num == 1:
        return 1
    elif num % 2 == 1:
        return num + is_polite(num - 1)
    else:
        return num + is_polite(num + 1)

def nth_polite_number(num):
    if num == 1:
        return 1
    else:
        return num + nth_polite_number(num - 1)

def nth_polite_number_recursive(num):
    if num == 1:
        return 1
    elif num % 2 == 1:
        return num + nth_polite_number_recursive(num - 1)
    else:
        return num + nth_polite_number_recursive(num + 1)

def nth_polite_number_iterative(num):
    num_polite = 1
    while num - 1 > 0:
        if num % 2 == 1:
            num_polite += num - 1
        else:
            num_polite += num + 1
        num -= 1
    return num_polite

print(nth_polite_number_recursive(7)) # 11
print(nth_polite_number_iterative(7)) # 11

"""
In the is_polite function, we check if the number is 1. If it is, we return 1, as 1 is the first polite number. If the number is odd, we add the number and call the function with the number reduced by 1. If the number is even, we add the number and call the function with the number increased by 1.

In the nth_polite_number function, we follow the same logic as the is_polite function, but instead of returning the result, we recurse until the number is 1.

In the nth_polite_number_recursive function, we follow the same logic as the nth_polite_number function, but instead of recursing, we use the recursion to calculate the result.

In the nth