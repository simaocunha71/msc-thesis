def digit_distance_nums(num1, num2):
    sum_diff = 0
    num1_str = str(num1)
    num2_str = str(num2)
    for i in range(min(len(num1_str), len(num2_str))):
        sum_diff += abs(int(num1_str[i]) - int(num2_str[i]))
    return sum_diff

print(digit_distance_nums(1,2)) # 1
assert digit_distance_nums(1,2) == 1
assert digit_distance_nums(123, 321) == 12
assert digit_distance_nums(12, 21) == 2
assert digit_distance_nums(345, 543) == 12
assert digit_distance_nums(1234, 4321) == 10
assert digit_distance_nums(1000, 2000) == 10
assert digit_distance_nums(10000, 20000) == 10
assert digit_distance_nums(100000, 200000) == 10
assert digit_distance_nums(123456, 654321) == 15
assert digit_distance_nums(1234567, 7654321) == 14
assert digit_distance_nums(12345678, 87654321) == 14
assert digit_distance_nums(123456789, 987654321) == 14
assert digit_distance_nums(100000000, 200000000) == 10
assert digit_distance_nums(1000000000, 2000000000) == 10
assert digit_distance_nums(10000000000, 20000000