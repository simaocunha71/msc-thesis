Here is a Python solution for the problem. It uses dynamic programming to efficiently compute the n-th element of the fibfib number sequence.

```Python
def fibfib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_sequence = [0, 0, 1]
        for i in range(3, n+1):
            fibfib_sequence.append(fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3])
        return fibfib_sequence[n]
```

This function works by first initializing a list `fibfib_sequence` with the first three elements of the sequence. It then enters a loop that continues until it has computed the n-th element of the sequence. In each iteration of the loop, it calculates the next element of the sequence as the sum of the previous three elements, and appends this new element to the `fibfib_sequence` list. Finally, it returns the n-th element of the `fibfib_sequence` list.

This function has a time complexity of O(n), which is much more efficient than a naive recursive solution that has a time complexity of O(2^n). The space complexity is also O(n), as we need to store the entire sequence in the `fibfib_sequence` list. However, this is still more efficient than a naive recursive solution that would require O(n) space to store the recursive function calls.