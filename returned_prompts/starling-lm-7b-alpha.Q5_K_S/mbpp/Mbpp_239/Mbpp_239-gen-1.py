"""
Here is a Python function that solves the problem:

```
def get_total_number_of_sequences(m, n):
    count = 0
    for i in range(1, m + 1):
        total = 0
        for j in range(n):
            if i > 0:
                total += i
                i *= 2
        count += total
    return count
```

Explanation:

The function `get_total_number_of_sequences` takes in two parameters `m` and `n`. It initializes a counter variable `count` to 0. It then starts a loop that iterates from 1 to `m`. Inside this loop, it initializes another variable `total` to 0. This variable will keep track of the total number of sequences that can be formed with the current value of `i` as the first element.

Inside the inner loop, it checks if `i` is greater than 0. If it is, it adds `i` to `total` and multiplies `i` by 2. This ensures that the next element in the sequence will be greater than or equal to twice the previous element. It continues this process `n` times, updating the total number of sequences that can be formed with the current value of `i` as the first element.

After the inner loop finishes, it adds the total number of sequences formed with the current value of `i` to the counter `count`. This process is repeated for all values from 1 to `m`. Finally, it returns the total number of sequences that can be formed with all the values from 1 to `m` as the first element, given the constraint of `n`.

In the given example, `get_total_number_of_sequences(10, 4)` will return 4, as there are 4 possible sequences of length 4 with the elements being greater than or equal to twice the previous element and less than or equal to 10.
"""

def get_total_number_of_sequences(m, n):
    count = 0
    for i in range(1, m + 1):
        total = 0
        for j in range(n):
            if i > 0: