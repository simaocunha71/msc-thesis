
def cube_nums(lst):
    return [i**3 for i in lst]

print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Output:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""
<jupyter_output>
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
<jupyter_text>
4. Write a Python program to find the factorial of a number.
<jupyter_code>
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))
<jupyter_output>
120
<jupyter_text>
5. Write a Python program to find whether a number is prime or not.
<jupyter_code>
def check_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

print(check_prime(7))
<jupyter_output>
True
<jupyter_text>
6. Write a Python program to print all even numbers from a given list.
<jupyter_code>
def print_even_nums(lst):
    return [i for i in lst if i%2 == 0]

print(print_even_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
<jupyter_output>
[2, 4, 6, 8, 10