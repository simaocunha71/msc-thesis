
    def sum_digits(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

    return sum(sum_digits(x) > 0 for x in arr)

print(count_nums([]))
print(count_nums([-1, 11, -11]))
print(count_nums([1, 1, 2]))

"""

# Solution:

def count_nums(arr):
    def sum_digits(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s
    return sum(sum_digits(x) > 0 for x in arr)

print(count_nums([])) # 0
print(count_nums([-1, 11, -11])) # 1
print(count_nums([1, 1, 2])) # 3

# Explanation:
# The function count_nums iterates over the input array arr, and for each element, it computes the sum of its digits using the helper function sum_digits. The function sum_digits works by repeatedly taking the remainder of the number divided by 10 (which gives the last digit) and adding it to the sum, then integer dividing the number by 10 (which removes the last digit). The function count_nums then counts the number of elements for which the sum of digits is greater than 0.

"""

# Solution:

def count_nums(arr):
    def sum_digits(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s
    return sum(sum_digits(x) > 0 for x in arr)

print(count_nums([])) # 0
print(count_nums([-1, 11, -11])) # 1
print(count_nums([1, 1, 2])) # 3

# Explanation:
# The function count_nums iterates over