def sum_of_divisors(n):
    if n == 0:
        return 0
    sum = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            sum += i + n//i
    return sum

# Test
assert sum_of_divisors(12)==28






"""
Write a function to calculate the sum of all elements of a given list of integers. The function should return zero if the list is empty.

For example, the sum of the elements of [1, 2, 3, 