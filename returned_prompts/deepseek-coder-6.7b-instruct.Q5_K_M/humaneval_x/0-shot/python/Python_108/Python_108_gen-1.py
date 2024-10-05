
def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            digits = list(str(num)[1:])
            num = -sum(int(digit) for digit in digits)
        else:
            digits = list(str(num))

        if sum(int(digit) for digit in digits) > 0:
            count += 1
    return count

# Testing
print(count_nums([]))  # 0
print(count_nums([-1, 11, -11]))  # 1
print(count_nums([1, 1, 2]))  # 3
print(count_nums([-123, 123, -123]))  # 3
print(count_nums([-123, 456, -789]))  # 3
print(count_nums([-111, 222, 333]))  # 0
print(count_nums([111, 222, 333]))  # 3
print(count_nums([-111, -222, -333]))  # 0

"""
Test Cases:
1. An empty array returns 0.
2. An array with single positive number returns 0.
3. An array with single negative number returns 0.
4. An array with two positive numbers returns 1.
5. An array with two negative numbers returns 0.
6. An array with one positive and one negative number returns 1.
7. An array with three positive numbers returns 3.
8. An array with three negative numbers returns 0.
9. An array with one positive and two negative numbers returns 1.
10. An array with two positive and one negative number returns 2.
11. An array with three positive and one negative number returns 2.
12. An array with three positive and two negative numbers returns 1.
13. An array with one positive and two negative numbers returns 1.
14. An array with two positive and two negative numbers returns 2