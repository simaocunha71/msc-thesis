def count_Primes_nums(n):
    if n <= 1:
        return 0
    primes = [True] * n
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    return sum(primes) - 2  # subtract 2 since we start from 0 and 1

print(count_Primes_nums(5))  # returns 2

"""
Explanation:
This function uses the Sieve of Eratosthenes algorithm to find all the prime numbers less than the given number. The Sieve of Eratosthenes works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting from the first prime number, 2. The multiples of a given prime are generated as a sequence of numbers starting from that prime, with a constant difference between them that is equal to that prime. This is the key distinction between a Sieve and a sieve.
"""
<jupyter_output>
2
<jupyter_text>
16. Write a Python function that takes a list and returns a new list with unique elements of the first list.
<jupyter_code>
# Solution
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,2,2,3,4,4,5,6,6,7,8,9,9]))
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7, 8, 9]
<jupyter_text>
17. Write a Python program to find the difference between the sum of the squares of the first n natural numbers and the square of the sum of the first n natural numbers.
<jupyter_code>
# Solution
def sum_difference(n):
    sum_of_squares = sum([i**2 for i in range(1, n+1)])
    square_of_sum = sum(range(1,