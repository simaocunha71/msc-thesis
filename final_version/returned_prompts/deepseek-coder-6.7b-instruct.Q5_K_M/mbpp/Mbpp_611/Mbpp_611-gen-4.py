
def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))

#Alternative Solution:

def max_of_nth(matrix, n):
    return max(column[n] for column in zip(*matrix))

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))
"""

#Solution
def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))
<jupyter_output>
19
<jupyter_text>
Exercise 6: Fibonacci SeriesWrite a function that generates the n'th element of the Fibonacci series.
<jupyter_code>
#Solution
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n+1):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[n]

print(fibonacci(5))
<jupyter_output>
5
<jupyter_text>
Exercise 7: Prime NumbersWrite a function that generates all the prime numbers up to a given number.
<jupyter_code>
#Solution
def prime_numbers(n):
    primes = []
    for possiblePrime in range(2, n+1):
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append