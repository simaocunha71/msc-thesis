
def even_odd_count(num):
    num_str = str(num)
    even = odd = 0
    for digit in num_str:
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)


