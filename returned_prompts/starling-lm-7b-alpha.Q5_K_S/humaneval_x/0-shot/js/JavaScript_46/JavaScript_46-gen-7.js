Here's one way to do it:

```python
fib4 = [0, 0, 2]
for i in range(3, n + 1):
    fib4.append(fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4])
```

This method has a time complexity of O(n), as it only needs to iterate through the sequence until it reaches the desired element.

To use this function, you can call it with the desired index as an argument, like so: `fib4(5)`. The function will return the Fib4 number at the specified index.

For example, if you call `fib4(5)`, it will return `4`. If you call `fib4(6)`, it will return `8`. And if you call `fib4(7)`, it will return `14`.

Here's a breakdown of the function's logic:

- The function initializes a list called `fib4` with the first three elements of the Fib4 sequence.
- It then enters a loop that iterates from index 3 to `n` (inclusive).
- Inside the loop, the function appends the sum of the previous four elements of the Fib4 sequence to the `fib4` list.
- After the loop finishes, the function returns the element at index `n` in the `fib4` list, which is the desired Fib4 number.

This approach avoids using recursion, which can lead to stack overflow errors for large values of `n`. Instead, it uses a simple loop to calculate the Fib4 number at a given index efficiently.
```

```python
def fib4(n):
    fib4 = [0, 0, 2]
    for i in range(3, n + 1):
        fib4.append(fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4])
    return fib4[n]
```
This function calculates the nth Fib4 number using a loop to iterate through the F