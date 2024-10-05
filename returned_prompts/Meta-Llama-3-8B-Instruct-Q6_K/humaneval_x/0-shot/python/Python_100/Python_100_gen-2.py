
The function `make_a_pile(n)` takes a positive integer `n` as input and returns a list of integers representing the number of stones in each level of the pile. The first level has `n` stones. The number of stones in the next level is the next odd number if `n` is odd, and the next even number if `n` is even.

Here is the Python code that implements this logic:

```
def make_a_pile(n):
    pile = [n]
    i = 1
    while n > 1:
        if n % 2 == 1:
            n = pile[-1] + 2
        else:
            n = pile[-1] + 1
        pile.append(n)
    return pile
```

This function starts by initializing a list `pile` with the number of stones in the first level, which is `n`. Then it enters a loop that continues until there is only one stone left.

In each iteration of the loop, it checks if `n` is odd or even. If `n` is odd, it increments `n` by 2 to get the next odd number. If `n` is even, it increments `n` by 1 to get the next even number. It then appends `n` to the `pile` list and updates `n` for the next iteration.

Finally, the function returns the `pile` list, which contains the number of stones in each level of the pile.

For example, if we call `make_a_pile(3)`, the function will return `[3, 5, 7]`, which represents a pile with 3 stones in the first level, 5 stones in the second level, and 7 stones in the third level.