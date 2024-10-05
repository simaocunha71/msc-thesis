
    def unique_digits(x):
        result = []
        for num in x:
            if all(int(digit) % 2 != 0 for digit in str(num)):
                result.append(num)
        return sorted(result)

    print(unique_digits([15, 33, 1422, 1]))
    print(unique_digits([152, 323, 1422, 10]))


The function `unique_digits` works by iterating over each number in the list `x`. For each number, it converts the number to a string and checks each digit of the number. If all the digits are odd (i.e., the remainder of dividing each digit by 2 is not zero), then the number is added to the `result` list. Finally, the `result` list is sorted in ascending order and returned.

Note: This solution assumes that all elements in the list are positive integers as per the problem statement.
"""


def unique_digits(x):
    result = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            result.append(num)
    return sorted(result)


print(unique_digits([15, 33, 1422, 1]))  # should return [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # should return []


# Additional test cases
print(unique_digits([1523, 323, 1422, 10]))  # should return [323, 10]
print(unique_digits([1523, 323, 1422, 10, 2]))  # should return [2, 323, 10]
print(unique_digits([1523, 323, 1422, 10, 20]))  # should return [323, 10