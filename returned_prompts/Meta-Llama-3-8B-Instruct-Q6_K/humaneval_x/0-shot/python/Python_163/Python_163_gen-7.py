```
def generate_integers(a, b):
    if a > b:
        a, b = b, a
    even_digits = [i for i in range(a, b+1) if int(str(i)[0]) % 2 == 0]
    return even_digits
```
Explanation:

1. First, we check if `a` is greater than `b`. If it is, we swap their values to ensure that `a` is less than or equal to `b`.
2. We then use a list comprehension to generate a list of even digits between `a` and `b` (inclusive). We do this by iterating over the range `a` to `b+1` (inclusive), and for each number `i` in that range, we check if the first digit of `i` (i.e., `int(str(i)[0])`) is even by checking if it's divisible by 2. If it is, we add `i` to the list of even digits.
3. Finally, we return the list of even digits.

Example inputs and outputs:

* `generate_integers(2, 8)` => `[2, 4, 6, 8]`
* `generate_integers(8, 2)` => `[2, 4, 6, 8]`
* `generate_integers(10, 14)` => `[]`

Note that the list comprehension is used to generate the list of even digits in a concise and efficient way. The `str(i)[0]` expression is used to extract the first digit of each number `i`, and the `int(...)` function is used to convert the first digit to an integer for comparison. The `range(a, b+1)` expression is used to generate the range of numbers from `a` to `b` (inclusive). The `if` statement inside the list comprehension is used to filter out the even digits from the range.