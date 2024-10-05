
def get_odd_collatz(n):
    collatz = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n % 2 != 0:
            collatz.append(n)
    return sorted(collatz)

print(get_odd_collatz(5))
<jupyter_output>
[1, 5]
<jupyter_text>
Problem 3 - Counting Characters In a String (10 Points)Write a Python function `count_chars` that accepts a string `s` and a character `c`. The function should return the number of times that character appears in the string.For example:```count_chars('hello', 'o') returns 1count_chars('hello', 'l') returns 2count_chars('hello', 'x') returns 0```
<jupyter_code>
