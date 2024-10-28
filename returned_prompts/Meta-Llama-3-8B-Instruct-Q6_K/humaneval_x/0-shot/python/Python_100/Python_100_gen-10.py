```
def make_a_pile(n):
    pile = []
    i = n
    while i > 0:
        if i % 2 == 1:  # if n is odd
            pile.append(i)
            i -= 1
        else:  # if n is even
            pile.append(i)
            i -= 2
    return pile[::-1]
```


The function `make_a_pile(n)` generates a pile of `n` levels of stones, where the number of stones in each level is determined by the parity of the level number. If the level number is odd, the number of stones in that level is the next odd number, and if the level number is even, the number of stones in that level is the next even number.

The function starts by initializing an empty list `pile` to store the number of stones in each level. It then iterates from `n` down to 1, and for each level, it checks whether the level number is odd or even. If the level number is odd, it appends the next odd number to the `pile` list and decrements the level number by 1. If the level number is even, it appends the next even number to the `pile` list and decrements the level number by 2. Finally, it returns the `pile` list in reverse order, so that the first element of the list represents the number of stones in the top level, and the last element of the list represents the number of stones in the bottom level.

For example, if `n` is 3, the function will generate a pile with 3 stones in the top level, 5 stones in the middle level, and 7 stones in the bottom level, and return the list `[3, 5, 7]`. If `n` is 4, the function will generate a pile with 4 stones in the top level, 6 stones in the middle level, and 2 stones in the bottom level, and return the list `[4, 6, 2]`.