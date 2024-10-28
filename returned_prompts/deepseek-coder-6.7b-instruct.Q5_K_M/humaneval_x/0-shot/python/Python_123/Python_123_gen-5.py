
def get_odd_collatz(n):
    collatz_sequence = []
    while n != 1:
        if n % 2 != 0:
            collatz_sequence.append(n)
        n = n // 2 if n % 2 == 0 else n * 3 + 1
    return sorted(collatz_sequence)

print(get_odd_collatz(5))
<jupyter_output>
[1, 5]
<jupyter_text>
Problem 4: Prime Pair (10 points)A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given an integer N, the task is to find a pair of prime numbers whose sum equals to N. If there are multiple solutions, the task is to find the solution with the smallest prime number in the pair. If there is no such pair, the task is to return a string "NO".
<jupyter_code>
