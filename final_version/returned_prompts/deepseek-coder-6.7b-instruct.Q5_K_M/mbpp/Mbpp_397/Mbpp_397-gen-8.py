def median_numbers(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    return numbers[1]

print(median_numbers(25,55,65))
assert median_numbers(25,55,65)==55.0

"""
