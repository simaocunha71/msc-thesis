The Newman-Conway sequence is a sequence of numbers where each number is the maximum of the previous number and the sum of the previous number and 1. 

The sequence starts with 1. The first 10 numbers in the sequence are: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.

Here is a Python function to find the nth number in the sequence:

```
def sequence(n):
    a = 1
    b = 1
    for _ in range(n-2):
        a, b = b, max(a, b) + 1
    return b
```

This function starts with the first two numbers in the sequence, `a` and `b`, both set to 1. It then enters a loop that continues `n-2` times, updating `a` and `b` in each iteration. In each iteration, `a` becomes `b` and `b` becomes the maximum of `a` and `b` plus 1. After the loop, `b` is the `n`th number in the sequence, which is returned by the function. 

For example, `sequence(10)` returns 6, which is the 10th number in the sequence. 