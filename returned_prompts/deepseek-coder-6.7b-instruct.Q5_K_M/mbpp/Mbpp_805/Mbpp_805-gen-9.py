def max_sum_list(lst):
    max_sum = max(sum(sub_list) for sub_list in lst)
    return [sub_list for sub_list in lst if sum(sub_list) == max_sum][0]

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))

# Output: [10, 11, 12]

# Explanation: The sum of elements in [10,11,12] is the highest among all sublists.
<jupyter_output>
[10, 11, 12]
<jupyter_text>
Q2:Given the string "Python Bootcamp", write a Python function that returns a string that is made up of the first and last characters of the given string.
<jupyter_code>
def first_last(s):
    return s[0] + s[-1]

print(first_last("Python Bootcamp"))

# Output: "Pyc"

# Explanation: The first character of "Python Bootcamp" is 'P' and the last character is 'c'.
<jupyter_output>
Pyc
<jupyter_text>
Q3:Write a Python function to find the factorial of a number.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Output: 120

# Explanation: The factorial of 5 is 5*4*3*2*1 = 120.
<jupyter_output>
120
<jupyter_text>
Q4:Write a Python function that takes a list of numbers and returns the sum of the squares of the even numbers in the list.
<jupyter_code>
def sum_squares_even(lst):
    return sum(n**2 for n in lst if n%2 == 