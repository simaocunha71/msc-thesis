
Here is one way to solve this problem:

1. Initialize a set called `odd_nums` to store the odd numbers we find.
2. Initialize an empty list called `collatz_seq`.
3. Initialize `curr_num` to be equal to `n`.
4. While `curr_num` is not equal to 1, perform the following steps:
    a. If `curr_num` is even, then append `curr_num` to `collatz_seq` and append `curr_num/2` to `odd_nums`. Then, set `curr_num` to `curr_num/2`.
    b. If `curr_num` is odd, then append `curr_num` to `collatz_seq` and append `3*curr_num+1` to `odd_nums`. Then, set `curr_num` to `3*curr_num+1`.
5. Append `1` to `collatz_seq`.
6. Sort `odd_nums` in increasing order.
7. Return `odd_nums`.

Here is the Python code that implements the above algorithm:

```python
def get_odd_collatz(n):
    odd_nums = set()
    collatz_seq = []
    curr_num = n

    while curr_num != 1:
        if curr_num % 2 == 0:
            collatz_seq.append(curr_num)
            odd_nums.add(curr_num//2)
            curr_num = curr_num//2
        else:
            collatz_seq.append(curr_num)
            odd_nums.add(3*curr_num + 1)
            curr_num = 3*curr_num + 1

    collatz_seq.append(1)
    sorted_odd_nums = sorted(odd_nums)

    return sorted_odd_nums
```

You can use this function to find the odd numbers in the Collatz sequence of any positive integer `n`. For example, if you call `get_odd_collatz(5)`, it will return `[1, 5]`, since the Collatz sequence for 5 is `