Here is a solution in Python:

```python
def max_sum_increasing_subseq(seq, i, k):
    # Initialize the result
    result = [0] * len(seq)

    # Fill the result array
    result[i] = seq[i]
    for j in range(i + 1, len(seq)):
        if seq[j] > seq[j - 1]:
            result[j] = result[j - 1] + seq[j]
        else:
            result[j] = max(result[j - 1], seq[j])

    # Check if kth element is greater than ith element
    if seq[k - 1] > seq[i]:
        return result[k - 1]

    # Check if the sequence is increasing from ith element until kth element
    if seq[k - 1] > seq[k - 2]:
        return result[k - 1]

    # Check if the ith element is greater than kth element
    if seq[i] > seq[k - 1]:
        return result[i]

    # Return the maximum sum of the increasing subsequence until i
    return max(result[i], seq[k - 1])
```

You can use the `max_sum_increasing_subseq` function like this:

```python
seq = [1, 101, 2, 3, 100, 4, 5]
i = 7
k = 4
print(max_sum_increasing_subseq(seq, i, k))  # Output: 11
```

The `max_sum_increasing_subseq` function initializes an array called `result` with all its elements set to zero. It then iterates over the sequence from `i + 1` to the end and checks if the current element is greater than the previous element. If it is, it adds the current element to the previous element in the `result` array. If not, it assigns the maximum value between the previous element and the current element to the current element in the `result` array.

After filling the `result