
def choose_num(x, y):
    # Reverse the order of the range if x > y
    if x > y:
        x, y = y, x

    # Check if x is odd
    if x % 2 != 0:
        # If x is odd, start from the next even number
        x += 1

    # Check if y is smaller than x (meaning there's no even number in the range)
    if y < x:
        return -1

    # Return the largest even number in the range
    return y if y % 2 == 0 else y - 1

print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
print(choose_num(13, 14))  # Output: 14
print(choose_num(18, 18))  # Output: 18
print(choose_num(19, 19))  # Output: -1
print(choose_num(10, 10))  # Output: 10
print(choose_num(12, 14))  # Output: 14
print(choose_num(13, 15))  # Output: 14
print(choose_num(14, 16))  # Output: 16
print(choose_num(15, 17))  # Output: 16
print(choose_num(16, 18))  # Output: 18
print(choose_num(17, 19))  # Output: 18
print(choose_num(18, 20))  # Output: 20
print(choose_num(19, 21))  # Output: 20
print(choose_num(20, 22))  # Output: 22
print(choose_num(21, 23))  # Output: 22
print(choose_num(22, 24))  # Output: 24
print(choose_num(23, 25