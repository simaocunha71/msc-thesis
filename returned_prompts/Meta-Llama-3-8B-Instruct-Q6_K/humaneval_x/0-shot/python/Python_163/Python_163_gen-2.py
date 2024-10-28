```
def generate_integers(a, b):
    if a > b:
        a, b = b, a
    even_digits = [i for i in range(a, b+1) if int(str(i)[0]) % 2 == 0]
    return even_digits
```
The function `generate_integers(a, b)` takes two positive integers `a` and `b` as input and returns a list of even digits between `a` and `b`, in ascending order. If `a` is greater than `b`, the function swaps their values. Then, it generates a list comprehension to iterate over the range from `a` to `b+1` (inclusive) and checks if each number is even by converting the number to a string, taking the first character, and checking if it's even using the modulo operator (`%`). The list of even digits is then returned.

For example, calling `generate_integers(2, 8)` will return `[2, 4, 6, 8]`, and calling `generate_integers(8, 2)` will also return `[2, 4, 6, 8]`, because the function swaps the values of `a` and `b` if necessary. Calling `generate_integers(10, 14)` will return an empty list, because there are no even digits between 10 and 14.