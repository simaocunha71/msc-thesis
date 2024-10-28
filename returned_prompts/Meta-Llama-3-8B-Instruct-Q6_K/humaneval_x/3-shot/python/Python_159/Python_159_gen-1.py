    total_eaten = number
    remaining -= number
    if remaining < need - number:
        total_eaten += remaining
        remaining = 0
    else:
        total_eaten += need - number
        remaining -= need - number

    return [total_eaten, remaining]  # [total number of eaten carrots, the number of carrots left]
# Test cases
print(eat(5, 6, 10))  # Output: [11, 4]
print(eat(4, 8, 9))  # Output: [12, 1]
print(eat(1, 10, 10))  # Output: [11, 0]
print(eat(2, 11, 5))  # Output: [7, 0]
print(eat(10, 5, 3))  # Output: [15, -2]  # Negative number of remaining carrots is not allowed
print(eat(0, 10, 10))  # Output: [10, 0]
print(eat(5, 5, 5))  # Output: [10, 0]
print(eat(1, 1, 1))  # Output: [2, 0]
print(eat(2, 2, 2))  # Output: [4, 0]
print(eat(3, 3, 3))  # Output: [6, 0]
print(eat(4, 4, 4))  # Output: [8, 0]
print(eat(5, 5, 5))  # Output: [10, 0]
print(eat(6, 6, 6))  # Output: [12, 0]
print(eat(7, 7, 7))  # Output: [14, 0]
print(eat(8, 8, 8))  # Output: [16, 0]
print(eat(9, 9, 9))  # Output: [18, 0]
print(eat(10, 10, 10))  # Output: [20, 0]
# print(eat(11, 11, 11))  # Output: [22, 0]
# print(eat(12, 12, 12))  # Output: [24, 0]
#