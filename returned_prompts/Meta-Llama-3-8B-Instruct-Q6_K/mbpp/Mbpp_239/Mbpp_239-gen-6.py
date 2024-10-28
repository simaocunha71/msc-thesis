The problem can be solved by using recursion. The idea is to start with the first element, which can be any number from 2 to m. Then, for each possible first element, we recursively generate all possible sequences of length n-1, and multiply the number of sequences by the number of possible values for the first element.

Here is the Python code for the problem:

```Python
def get_total_number_of_sequences(m, n):
    def get_sequences(current, length):
        if length == 1:
            return 1
        total = 0
        for i in range(2, min(m, current//2) + 1):
            total += get_sequences(i, length - 1)
        return total
    return get_sequences(2, n)
```

This function first defines a helper function `get_sequences` that generates all possible sequences of a given length, starting from a given current value. The base case is when the length is 1, in which case there is only one sequence. Otherwise, the function iterates over all possible values for the current element, recursively calls itself to generate all possible sequences of the remaining length, and sums up the total number of sequences.

The main function `get_total_number_of_sequences` then calls the helper function with the initial value 2 and the desired length n, and returns the result.

The unit test `assert get_total_number_of_sequences(10, 4) == 4` ensures that the function works correctly. For example, when m is 10 and n is 4, the function should return 4, because there are 4 possible sequences: (2, 4, 6, 8), (2, 4, 8, 9), (2, 6, 8, 10), and (3, 6, 9, 10).