
def unique_digits(x):
    def has_even_digit(num):
        return any(int(digit) % 2 == 0 for digit in str(num))

    return sorted([num for num in x if not has_even_digit(num)])

print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # []

Explanation:

The function unique_digits takes a list of positive integers as input. It defines an inner function has_even_digit that checks if a number has an even digit. It then uses a list comprehension to create a new list that includes only the numbers from the original list that have no even digits. The resulting list is then sorted and returned.

The inner function uses a generator expression to iterate over each digit in the number, converts it to an integer, and checks if it's even. If it finds an even digit, it returns True; otherwise, it returns False. The any function then returns True if any of the digits were even, and False otherwise.

The outer function uses this to create a new list that includes only the numbers from the original list that have no even digits, and returns this sorted list.

This solution has a time complexity of O(n*m) where n is the number of elements in the input list and m is the average number of digits in the numbers. It also has a space complexity of O(n) for the output list.

I hope this explanation makes it clear how this solution works. Let me know if you have any other questions.
"""

# Solution 2:
"""
