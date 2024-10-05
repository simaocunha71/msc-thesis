```
def make_a_pile(n):
    pile = [n]
    for i in range(1, n):
        if n % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```


Example usage:
```
print(make_a_pile(3))  # Output: [3, 5, 7]
```


Explanation:

1. Initialize an empty list `pile` to store the number of stones in each level.
2. Add the initial number of stones `n` to the list.
3. Iterate from 1 to `n-1`.
4. For each iteration, check if `n` is odd or even.
5. If `n` is odd, add the next odd number (which is 2 more than the current number) to the list.
6. If `n` is even, add the next even number (which is 1 more than the current number) to the list.
7. Return the list `pile` containing the number of stones in each level.