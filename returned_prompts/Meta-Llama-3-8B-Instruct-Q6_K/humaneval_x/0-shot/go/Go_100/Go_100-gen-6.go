The function MakeAPile(n) will return a list of integers representing the number of stones in each level of the pile. The list will start with the input number n and continue with the next odd or even number for each subsequent level.

Here's a Python solution for the problem:

```
def MakeAPile(n):
    pile = [n]
    i = 1
    while n > 1:
        if n % 2 == 1:
            n = n - i
            i += 2
        else:
            n = n - i
            i += 1
        if n > 0:
            pile.append(n)
    return pile
```

This function initializes a list called pile with the input number n. It then enters a while loop that continues until n becomes 1. Inside the loop, it checks whether n is odd or even. If n is odd, it subtracts the next odd number from n and increments the counter i by 2. If n is even, it subtracts the next even number from n and increments the counter i by 1. If n becomes 0 or less, the loop breaks and the function returns the pile list. The pile list represents the number of stones in each level of the pile, with the input number n being the first element in the list.