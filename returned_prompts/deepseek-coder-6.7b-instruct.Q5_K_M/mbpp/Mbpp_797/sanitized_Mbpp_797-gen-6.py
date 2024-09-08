def sum_in_range(l, r):
    odd_numbers = [num for num in range(l, r+1) if num % 2 != 0]
    return sum(odd_numbers)