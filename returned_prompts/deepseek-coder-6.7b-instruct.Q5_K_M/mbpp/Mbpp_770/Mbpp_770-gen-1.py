
def odd_num_sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**4
    return sum

print(odd_num_sum(2))

"""
Explaination:

In this function, we are using a for loop to calculate the fourth power of each odd number up to the nth odd number. We add these to the sum variable.

The range function is used to generate the sequence of odd numbers, starting from 1 (which is the first odd number), increasing by 2 each time (to get the next odd number), and stopping before the nth odd number (which is 2n-1).

The final sum is then returned by the function.

In the example provided, the function is called with the argument 2, so it calculates the fourth power of the first 2 odd numbers (1 and 3) and returns their sum (1^4 + 3^4 = 82).
"""
<jupyter_output>
82
<jupyter_text>
Q4. Write a python function to find the sum of fourth power of first n odd natural numbers.
<jupyter_code>
def odd_num_sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**4
    return sum

print(odd_num_sum(2))
<jupyter_output>
82
<jupyter_text>
Q5. Write a Python function which checks whether a passed string is palindrome or not.
<jupyter_code>
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('madam'))
<jupyter_output>
True
<jupyter_text>
Q6. Write a Python program which accepts a sequence of comma-separated numbers from user and generates a list and a tuple with those numbers.
<jupyter_code>
numbers = input("Enter comma-separated numbers: ")
numbers_list = numbers.split(',')
numbers_tuple = tuple(