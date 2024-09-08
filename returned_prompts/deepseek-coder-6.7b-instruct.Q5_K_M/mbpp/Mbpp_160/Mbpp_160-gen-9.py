def find_solution(a, b, n):
    if a == 0:
        if n % b == 0:
            return (0, n // b)
        else:
            return None
    if b == 0:
        if n % a == 0:
            return (n // a, 0)
        else:
            return None
    
    if a > b:
        q, r = divmod(n, a)
        if r == 0:
            return (0, q)
        x = find_solution(b % a, a, r)
        if x is not None:
            y = (q - x[1]*b//a)
            return (x[0] + y*b//a, y)
        else:
            return None
    else:
        q, r = divmod(n, b)
        if r == 0:
            return (q, 0)
        x = find_solution(a % b, b, r)
        if x is not None:
            y = (q - x[0]*a//b)
            return (x[0], x[1] + y*a//b)
        else:
            return None

# testing the function
print(find_solution(2, 3, 7)) # should return (2, 1)

# this function works by using the Euclidean algorithm to find the greatest common divisor (gcd) of a and b,
# and then using the gcd to find the x and y that satisfy the given equation.
# the gcd is found by using the modulo operation and recursive calls.
# if no solution exists, the function returns None.
<jupyter_output>
(2, 1)
<jupyter_text>
Q2. Write a Python function that takes a string and returns the number of vowels in that string.
<jupyter_code>
def count_vowels(s):
    return sum(map(s.lower().count, "aeiou"))

# testing the function
print(count_vowels("Hello World")) # should return 3
<jupyter_output>
