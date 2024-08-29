def is_samepatterns(colors, patterns):
    return all(patterns[i] == patterns[i + 1] for i in range(len(patterns) - 1))

print(is_samepatterns(["red","green","green"],  ["a",  "b", "b"]))

"""
This function uses a generator expression to check if all adjacent elements in the patterns list are equal. The all() function returns True only if all elements in the generator expression are True.

The function is_samepatterns(["red","green","green"], ["a","b","b"]) returns True, because all adjacent elements in the patterns list are equal.
"""
<jupyter_output>
True
<jupyter_text>
Q2. Write a function that returns the sum of multiples of 3 and 5 that are less than 1000.
<jupyter_code>
def sum_multiples():
    return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)

print(sum_multiples())
<jupyter_output>
234168
<jupyter_text>
Q3. Write a function to find the largest palindrome made from the product of two 3-digit numbers.
<jupyter_code>
def largest_palindrome():
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if str(product) == str(product)[::-1] and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

print(largest_palindrome())
<jupyter_output>
906609
<jupyter_text>
Q4. Write a function to find the sum of all the prime numbers that are less than 2000.
<jupyter_code>
def is_prime(n):
    if n < 2:
        return False
    if n