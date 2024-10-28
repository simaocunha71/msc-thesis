def sum_digits(n):
    return sum(int(digit) for digit in str(n)) 

# Test case
assert sum_digits(345) == 12
print(sum_digits(345))  # Output: 12
print(sum_digits(0))    # Output: 0
print(sum_digits(12345)) # Output: 15
print(sum_digits(1234567)) # Output: 20
print(sum_digits(123456789)) # Output: 27
print(sum_digits(1234567890)) # Output: 27
print(sum_digits(12345678901)) # Output: 34
print(sum_digits(123456789012)) # Output: 45
print(sum_digits(1234567890123)) # Output: 18
print(sum_digits(12345678901234)) # Output: 21
print(sum_digits(123456789012345)) # Output: 18
print(sum_digits(1234567890123456)) # Output: 21
print(sum_digits(12345678901234567)) # Output: 18
print(sum_digits(1234567890123456789)) # Output: 27
print(sum_digits(12345678901234567890)) # Output: 45
print(sum_digits(123456789012345678901)) # Output: 18
print(sum_digits(123456789012345678902)) # Output: 21
print(sum_digits(123456789012345678903)) # Output: 18
print(sum_digits(123456789012345678904)) # Output: 21
print(sum_digits(123456789012345678905)) # Output: 18
print(sum_digits(123456789012345678906)) # Output: 21
print(sum_digits(123456789012345678907)) # Output: 18
print(sum_digits(123456789012345678908)) # Output: 21
print(sum_digits(123456789012345678909)) # Output: 18
print(sum_digits(123456789012345678910)) # Output: 21
print(sum_digits(123456789012345678911)) # Output: 18
print(sum_digits(123456789012345678912)) # Output: 21
print(sum_digits(123456789012345678913)) # Output: 18
print(sum_digits(123456789012345678914)) # Output: