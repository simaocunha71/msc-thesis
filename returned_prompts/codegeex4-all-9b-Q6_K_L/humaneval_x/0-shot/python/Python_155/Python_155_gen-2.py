def even_odd_count(num):
    num = str(abs(num))
    even = sum(1 for digit in num if int(digit) % 2 == 0)
    odd = sum(1 for digit in num if int(digit) % 2 == 1)
    return (even, odd)

print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)