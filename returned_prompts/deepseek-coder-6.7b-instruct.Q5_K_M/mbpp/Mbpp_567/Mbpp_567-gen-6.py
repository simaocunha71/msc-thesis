
def issort_list(list_):
    return all(list_[i] <= list_[i + 1] for i in range(len(list_) - 1))

print(issort_list([1,2,4,6,8,10,12,14,16,17]))

"""
This function works by iterating through the list and checking if the current element is less than or equal to the next one. If it is, then the function continues to the next pair of elements. If it finds a pair where the current element is greater than the next one, it immediately returns False and the function stops there. If it goes through the entire list without finding any such pair, it returns True. This means that the list is sorted.
"""
<jupyter_output>
True
<jupyter_text>
3. Write a function called `get_digits` that takes an integer as an argument and returns a list of its digits. The digits should be in the same order as they appear in the integer.For example:```get_digits(12345)```would return `[1, 2, 3, 4, 5]`.
<jupyter_code>
def get_digits(n):
    return [int(i) for i in str(n)]

print(get_digits(12345))
<jupyter_output>
[1, 2, 3, 4, 5]
<jupyter_text>
4. Write a function called `is_prime` that takes an integer as an argument and returns `True` if the integer is a prime number and `False` otherwise.
<jupyter_code>
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
<jupyter_output>
True
False
<jupyter_text>
5. Write a function called `filter_primes