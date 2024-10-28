To solve this problem, we can use a dictionary (or hashmap) to keep track of the numbers we have seen so far. For each number in the list, we check if the difference between zero and that number is in the dictionary. If it is, then we have found a pair of distinct elements that sum to zero and we return true. If it's not, then we add the number to the dictionary. If we go through the entire list without finding a pair of distinct elements that sum to zero, we return false.

Here's a step-by-step explanation of the solution:

1. Initialize an empty dictionary called `seen`.
2. Iterate through each number in the input list `l`.
3. For each number, check if the difference between zero and that number (`-num`) is in the `seen` dictionary. If it is, then we have found a pair of distinct elements that sum to zero, so we return `true`.
4. If `-num` is not in the `seen` dictionary, add the current number to the `seen` dictionary.
5. After iterating through all the numbers in the list, if we haven't found a pair of distinct elements that sum to zero, return `false`.

Here's the code for the solution:

```python
def pairsSumToZero(l):
    seen = {}
    for num in l:
        if -num in seen:
            return True
        else:
            seen[num] = True
    return False
```

You can test the function with the provided test cases to see if it works correctly:

```python
print(pairsSumToZero([1, 3, 5, 0]))  # False
print(pairsSumToZero([1, 3, -2, 1]))  # False
print(pairsSumToZero([1, 2, 3, 7]))  # False
print(pairsSumToZero([2, 4, -5, 3, 5, 7]))  # True
print(pairsSumToZero([1]))  # False
```

The output of these test cases should match the expected results provided in the question.

I hope this helps! Let me know if you have any more questions.

-