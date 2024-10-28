
The function `generate_integers(a, b)` takes two positive integers `a` and `b` as input and returns a list of even digits between `a` and `b`, in ascending order.

Here's the step-by-step implementation:

1. Initialize an empty list `result` to store the even digits.
2. Use a for loop to iterate over the range of integers from the minimum of `a` and `b` to the maximum of `a` and `b` (inclusive).
3. For each integer `i` in the range, check if it's even by using the modulo operator (`i % 2 == 0`).
4. If `i` is even, append it to the `result` list.
5. Finally, return the `result` list.

Note that the `min` and `max` functions are used to ensure that the range starts from the smaller of `a` and `b` and ends at the larger of `a` and `b`. This is because the problem statement doesn't specify the order of `a` and `b`, so we need to handle both cases.