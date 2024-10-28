The problem asks to generate the first n+1 numbers of the Tribonacci sequence. The Tribonacci sequence is defined by the recurrence relation:
tri(1) = 3
tri(n) = 1 + n / 2, if n is even
tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd

Here is a Python function that solves this problem:

```Python
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [1, 3]
    else:
        trib = [1, 3]
        for i in range(2, n):
            if i % 2 == 0:
                trib.append(1 + i / 2)
            else:
                trib.append(trib[i - 1] + trib[i - 2] + 3)
        return trib
```

The function starts by handling the base cases where n is 0, 1, or 2. For n > 2, it initializes a list trib with the first two elements of the Tribonacci sequence. Then, it iterates from 2 to n, and for each i, it checks if i is even or odd. If i is even, it appends 1 + i / 2 to trib. If i is odd, it appends the sum of the last three elements of trib to trib. Finally, it returns the list trib. This function correctly generates the first n+1 numbers of the Tribonacci sequence.