
def even_odd_count(num):
    count_even = 0
    count_odd = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd
