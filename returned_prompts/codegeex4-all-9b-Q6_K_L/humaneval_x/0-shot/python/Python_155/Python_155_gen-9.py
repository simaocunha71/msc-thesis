def even_odd_count(num):
    num = str(abs(num)) # convert to string and remove any negative sign
    even_count = sum(1 for digit in num if int(digit) % 2 == 0) # count even digits
    odd_count = sum(1 for digit in num if int(digit) % 2 != 0) # count odd digits
    return (even_count, odd_count)

# test cases
print(even_odd_count(-12)) # (1, 1)
print(even_odd_count(123)) # (1, 2)