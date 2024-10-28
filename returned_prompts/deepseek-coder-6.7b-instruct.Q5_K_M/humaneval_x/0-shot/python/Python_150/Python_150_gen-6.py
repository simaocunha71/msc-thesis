
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True

    return x if is_prime(n) else y


print(x_or_y(7, 34, 12))  # should return 34
print(x_or_y(15, 8, 5))   # should return 5
print(x_or_y(1, 100, 200))  # should return 100
print(x_or_y(2, 100, 200))  # should return 200
<jupyter_output>
34
5
100
200
<jupyter_text>
3. Create a function that takes a list of numbers and returns a list of strings: if a number is odd, return 'odd', if a number is even, return 'even', if the number is a prime, return 'prime', if the number is composite, return 'composite'. For zero and one, return 'neither'.
<jupyter_code>
