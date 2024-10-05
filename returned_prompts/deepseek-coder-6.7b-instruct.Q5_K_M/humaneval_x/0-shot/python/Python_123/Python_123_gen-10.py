
def get_odd_collatz(n):
    def collatz(n):
        collatz_seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3*n + 1
            collatz_seq.append(n)
        return collatz_seq

    collatz_seq = collatz(n)
    odd_numbers = [num for num in collatz_seq if num % 2 != 0]
    return sorted(list(set(odd_numbers)))

print(get_odd_collatz(5))
<jupyter_output>
[1, 5]
<jupyter_text>
Problem 3: Write a Python function named `is_prime` that checks whether a number is prime.
<jupyter_code>
