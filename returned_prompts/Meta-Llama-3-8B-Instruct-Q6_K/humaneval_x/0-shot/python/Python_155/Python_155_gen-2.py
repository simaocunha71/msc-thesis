
The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits in the integer. Here's the solution:

```
def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
```

Here's an explanation of the code:

1. We initialize two counters, `even_count` and `odd_count`, to keep track of the number of even and odd digits, respectively.
2. We convert the input integer to a string using the `str()` function. This allows us to iterate over each digit in the integer.
3. We iterate over each digit in the string using a `for` loop. For each digit, we check if it's even or odd by using the modulo operator (`%`). If the remainder is 0, the digit is even; otherwise, it's odd.
4. If the digit is even, we increment the `even_count` counter. If the digit is odd, we increment the `odd_count` counter.
5. Finally, we return a tuple containing the `even_count` and `odd_count` counters.

Here's an example usage of the function:

```
>>> even_odd_count(-12)
(1, 1)
>>> even_odd_count(123)
(1, 2)
```

In the first example, the input is `-12`, and the output is `(1, 1)`, indicating that there is one even digit (`2`) and one odd digit (`1`).

In the second example, the input is `123`, and the output is `(1, 2)`, indicating that there is one even digit (`3`) and two odd digits (`1` and `3`). Note that the output is correct even though the input is a negative integer, since we used the `abs()` function to convert the input to a positive integer before processing it.