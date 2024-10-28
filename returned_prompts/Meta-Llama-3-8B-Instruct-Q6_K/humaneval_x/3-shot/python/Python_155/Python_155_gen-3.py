    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
# test the function
print(even_odd_count(-12))  # (1, 1)
print(even_odd_count(123))  # (1, 2)  # test the function with different inputs


