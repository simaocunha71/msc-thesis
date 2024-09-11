from math import sqrt
def count_Primes_nums(x):
    if x < 2:
        return 0
    sqrt_x = int(sqrt(x))
    table = [True] * (sqrt_x + 1)
    table[0] = False
    table[1] = False
    for i in range(2, sqrt_x + 1):
        if table[i]:
            for j in range(i * i, sqrt_x + 1, i):
                table[j] = False
    return sum(table)

# assert count_Primes_nums(5) == 2

"""
This function works by first checking if the given input x is less than 2. Since there are no prime numbers less than 2, we return 0 if that is the case.
Next, we calculate the square root of x and store it in sqrt_x. This is because in order to check if a number is prime, we only need to check up to its square root.
We create a boolean list called "table" which is initially filled with True values. We use this list to keep track of whether a number is prime or not.
We set table[0] and table[1] to False since 0 and 1 are not prime numbers.
Next, we iterate through the list from index 2 to sqrt_x + 1. For each index i, if the corresponding value in table is True, then the number at index i is a prime number. We set it to False and then iterate through all the multiples of i starting from i * i and incrementing by i. For each multiple, we set the corresponding value in table to False. This way, we mark all the non-prime numbers as False in the table.
Finally, we return the sum of the table. Since all the False values represent non-prime numbers, the sum of the table represents the count of prime numbers less than x.
"""

```python
# Python program to count prime numbers

# Function to count prime numbers
def count_Primes_nums(x):
    if x < 2:
        return 0
    sqrt_x = int(sqrt(x))
    table = [True] * (sqrt_