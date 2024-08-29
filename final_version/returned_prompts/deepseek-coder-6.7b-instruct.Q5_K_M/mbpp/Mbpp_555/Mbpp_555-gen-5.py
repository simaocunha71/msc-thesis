def difference(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_numbers = sum(i for i in range(1, n+1))
    return sum_of_cubes - sum_of_numbers

print(difference(3))
<jupyter_output>
30
<jupyter_text>
Question 2:Write a Python function to find the sum of all the multiples of 3 or 5 below 100.
<jupyter_code>
def sum_multiples(n):
    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)

print(sum_multiples(100))
<jupyter_output>
2318
<jupyter_text>
Question 3:Write a Python function to find the largest prime factor of a given number.
<jupyter_code>
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(largest_prime_factor(600851475143))
<jupyter_output>
6857
<jupyter_text>
Question 4:Write a Python function to check if a string is a palindrome.
<jupyter_code>
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('madam'))
<jupyter_output>
True
<jupyter_text>
Question 5:Write a Python function to find all the factors of a given number.
<jupyter_code>
def find_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

print(find_factors(100))
<jupyter_output>
[1, 2