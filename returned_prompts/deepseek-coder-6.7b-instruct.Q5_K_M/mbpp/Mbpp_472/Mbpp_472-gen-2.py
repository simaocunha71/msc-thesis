def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst)+1))

print(check_Consecutive([1,2,3,4,5])) # True

"""
This function works by first sorting the list and then checking if the sorted list is the same as a list of consecutive numbers from the minimum value of the original list to the maximum value of the original list.
"""
<jupyter_output>
True
<jupyter_text>
Q2: Write a python function to calculate the factorial of a number.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) # 120
<jupyter_output>
120
<jupyter_text>
Q3: Write a python function to generate a list of Fibonacci numbers upto n.
<jupyter_code>
def generate_Fibonacci(n):
    fib_list = [0, 1]
    while fib_list[-1] < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:-1]

print(generate_Fibonacci(20)) # [0, 1, 1, 2, 3, 5, 8, 13]
<jupyter_output>
[0, 1, 1, 2, 3, 5, 8, 13]
<jupyter_text>
Q4: Write a python function to check if a string is a palindrome or not.
<jupyter_code>
def check_palindrome(s):
    return s == s[::-1]

print(check_palindrome('radar')) # True
<jupyter_output>
True
<jupyter_text>
Q5: Write a python function to generate a list of prime numbers upto n