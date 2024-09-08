def big_diff(lst):
    return max(lst) - min(lst)

print(big_diff([1,2,3,4]))
<jupyter_output>
3
<jupyter_text>
3. Write a Python function to find the sum of all elements in a list.
<jupyter_code>
def sum_list(lst):
    return sum(lst)

print(sum_list([1,2,3,4]))
<jupyter_output>
10
<jupyter_text>
4. Write a Python function to get the largest and smallest number from a list.
<jupyter_code>
def get_max_min(lst):
    return max(lst), min(lst)

print(get_max_min([1,2,3,4]))
<jupyter_output>
(4, 1)
<jupyter_text>
5. Write a Python function to check if a number is prime or not.
<jupyter_code>
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(5))
<jupyter_output>
True
<jupyter_text>
6. Write a Python function to return the factorial of a number.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
<jupyter_output>
120
<jupyter_text>
7. Write a Python function to return the number of prime numbers that exist up to a given number.
<jupyter_code>
def count_