def digit_distance_nums(num1, num2):
    d1 = [int(i) for i in str(num1)]
    d2 = [int(i) for i in str(num2)]
    ld1 = len(d1)
    ld2 = len(d2)
    if ld1 != ld2:
        return -1
    sum = 0
    for i in range(ld1):
        sum += abs(d1[i] - d2[i])
    return sum
# Testing the function
print(digit_distance_nums(1, 2))  # should print 1

# Testing the function for different inputs
print(digit_distance_nums(123, 456))  # should print 7
print(digit_distance_nums(12345, 67890))  # should print 25
print(digit_distance_nums(123456, 987654))  # should print 39
print(digit_distance_nums(123456, 123456))  # should print 0
print(digit_distance_nums(123456, 123457))  # should print 1
print(digit_distance_nums(123456, 123459))  # should print 4

# Testing the function with negative numbers
print(digit_distance_nums(-123456, 123456))  # should print 39
print(digit_distance_nums(-123456, -123456))  # should print 0

# Testing the function with zero
print(digit_distance_nums(0, 0))  # should print 0
print(digit_distance_nums(0, 1))  # should print 1
print(digit_distance_nums(0, -1))  # should print 1

# Testing the function with very large numbers
print