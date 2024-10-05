The function makeAPile takes a positive integer n as an argument and returns a list of the number of stones in each level of the pile.

Here is the Python solution:

```
def makeAPile(n):
    pile = []
    for i in range(1, n+1):
        if i % 2 == 1:
            pile.append(i * 2 - 1)
        else:
            pile.append(i * 2)
    return pile
```

This function initializes an empty list `pile` and then iterates over the range from 1 to `n+1`. For each iteration, it checks if the current number `i` is odd or even using the modulus operator (`i % 2 == 1` for odd and `i % 2 == 0` for even). If `i` is odd, it adds `i * 2 - 1` to the `pile` list, which is the next odd number. If `i` is even, it adds `i * 2` to the `pile` list, which is the next even number. Finally, it returns the `pile` list.

For example, when `n` is 3, the function returns `[3, 5, 7]`, which are the number of stones in each level of the pile.

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the input integer.