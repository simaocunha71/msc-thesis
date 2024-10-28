
def even_odd_count(num):
    # Create a list of digits
    digits = [int(digit) for digit in str(abs(num))]

    # Count even and odd digits
    even = 0
    odd = 0
    for digit in digits:
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1

    return (even, odd)