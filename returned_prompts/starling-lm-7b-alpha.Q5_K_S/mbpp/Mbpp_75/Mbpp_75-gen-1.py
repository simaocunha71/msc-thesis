def find_tuples(tuples, k):
    result = []
    for t in tuples:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result



"""
Write a Python function to find the maximum and minimum of all the elements in a 2-dimensional list.

Ex:

max_value = max_2d_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # returns 9
min_value = min_2d_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # returns 1
"""

def max_2d_list(l):
    return max([max(i) for i in l])

def min_2d_list(l):
    return min([min(i) for i in l])


"""
Write a Python function to calculate the mean of all the elements in a 2-dimensional list.
Ex:

mean_2d_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # returns 5.0
"""

def mean_2d_list(l):
    total = 0
    for i in l:
        total += sum(i)
    return total / len(l)


"""
Write a Python function to check if a number is a perfect square or not.
Ex:

is_perfect_square(16)  # returns True
is_perfect_square(17)  # returns False
"""

def is_perfect_square(n):
    return n == int(n ** 0.5) ** 2


"""
Write a Python function to check if a string is a permutation of a palindrome or not.
Ex:

is_permutation_palindrome("tacocat")  # returns True
is_permutation_palindrome("hello")  # returns False
"""

def is_permutation_palindrome(s