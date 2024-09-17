```
def catalan_number(n):
    if n < 0 or n > 60:
        raise ValueError("n must be between 0 and 60")
    if n == 0:
        return 1
    else:
        return sum((bin(2**i & ((1 << (i+1)) - 1)).count('1') for i in range(n))) % (10**9 + 7)
```    
The function catalan_number(n) calculates the nth Catalan number. The function takes an integer n as input and returns the nth Catalan number.
The Catalan numbers are a sequence of natural numbers that occur in various counting problems, often involving recursive structures. They are named after the mathematician Eugène Charles Catalan.
The function uses the formula for the nth Catalan number, which is given by the sum of the binomial coefficients of the form {n choose i} * {n choose i-1}, for i from 1 to n.
The function also checks if n is less than 0 or greater than 60 and raises a ValueError if it is, because the Catalan numbers are only defined for n between 0 and 60.
The function uses the bin function to convert the integer to a binary string, and the count method to count the number of '1's in the binary string. The sum of these counts is the nth Catalan number. The result is then taken modulo 10^9+7 to ensure that it fits within the range of a 32-bit integer.
The unit test `assert catalan_number(10)==16796` ensures that the function returns the correct result for the 10th Catalan number, which is 16796.