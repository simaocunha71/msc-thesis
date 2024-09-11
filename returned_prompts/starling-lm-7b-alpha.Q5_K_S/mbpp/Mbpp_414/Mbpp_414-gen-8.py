def overlapping(seq1, seq2):
    for i in seq1:
        if i in seq2:
            return True
    return False

# test
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False







"""
Write a python function to count the number of elements in a given list, which are multiples of a given number
"""
def multiple(nums, n):
    counter = 0
    for i in nums:
        if i % n == 0:
            counter += 1
    return counter

# test
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(multiple(nums, 2))



"""
Write a Python function to check whether a number is a prime number or not
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# test
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))


"""
Write a Python function to calculate the factorial of a number
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# test
print(factorial(0))
print(factorial(1))
print(factorial(5))


"""
Write a Python function to calculate the sum of squares of the first n natural numbers
"""
def sum_sq(n):
    return (n * (n + 1) * (2 * n + 1)) / 6

# test
print(sum_sq(0))
print(sum_sq(1))
print(sum_sq(5))


"""
Write a Python function to calculate the sum of squares of the first n natural numbers without using any loop or