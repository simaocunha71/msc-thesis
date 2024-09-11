def digit_distance_nums(num1, num2):
    num_str1 = str(num1)
    num_str2 = str(num2)
    if len(num_str1) != len(num_str2):
        raise ValueError("The two numbers must be the same length")
    return sum(abs(int(num_str1[i]) - int(num_str2[i])) for i in range(len(num_str1)))

# Testing
assert digit_distance_nums(1,2) == 1

# Testing edge cases
try:
    digit_distance_nums(9, 10)
except ValueError as e:
    assert str(e) == "The two numbers must be the same length"
try:
    digit_distance_nums(999, 1)
except ValueError as e:
    assert str(e) == "The two numbers must be the same length"
try:
    digit_distance_nums(999999999999999999999999999, 9999999999999999999999999999)
except ValueError as e:
    assert str(e) == "The two numbers must be the same length"
try:
    digit_distance_nums(99999999999999999999999999999999999999999999, 9999999999999999999999999999999999999999999)
except ValueError as e:
    assert str(e) == "The two numbers must be the same length"

# Testing non-integer inputs
try:
    digit_distance_nums(9.99, 9.99)
except ValueError as e:
    assert str(e) == "The two numbers must be the same length"
try:
    digit_distance_nums(999