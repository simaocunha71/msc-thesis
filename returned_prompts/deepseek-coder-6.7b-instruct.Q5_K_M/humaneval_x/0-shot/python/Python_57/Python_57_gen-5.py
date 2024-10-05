
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or \
           all(l[i] >= l[i + 1] for i in range(len(l) - 1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()


In the function, we use the built-in all() function to check if all elements in the list are monotonically increasing or decreasing. The all() function returns True if all elements in the iterable are true. If not, it returns False. In our case, we provide two arguments to all() function: one for checking if all elements in the list are less than or equal to the next one (for increasing case), and the other for checking if all elements in the list are greater than or equal to the next one (for decreasing case). If either condition is met, the function returns True, indicating that the list elements are monotonically increasing or decreasing. Otherwise, it returns False.

We run the test using doctest module, which checks if the function output matches the expected output in the function comments. If there is a match, the test passes, otherwise it fails.
"""

# 1.1:
# What is the output of the following Python program?

"""
def foo(x, y):
    def bar(x):
        return x + 1
    return bar(y)

print(foo(1, 2))
"""
# Output: 3


# 1.2:
# Write a Python function that takes a list of integers and returns the sum of all even numbers in the list.

def sum_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)

# Test the function
print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: 12


# 1.3:
# Write a Python function that takes a string and returns a new string with all the words reversed in order.

def reverse_words(s):
    return ' '.join(s.split()[::-1])

#