You can solve this problem with the following function:

```python
def overlapping(sequence1, sequence2):
    for value in sequence1:
        if value in sequence2:
            return True
    return False
```


This function iterates over each value in the first sequence and checks if that value is present in the second sequence. If it finds a match, it returns True. If it doesn't find any matches after checking all values in the first sequence, it returns False. 

The unit test `assert overlapping([1,2,3,4,5],[6,7,8,9]) == False` ensures that the function correctly returns False when there are no overlapping values. This means that the function should return the expected result for all possible input combinations. 

However, if you want to check if any two sequences have at least one overlapping value, you can use the following function:

```python
def overlapping(sequence1, sequence2):
    return any(value in sequence2 for value in sequence1)
```


This function uses the built-in `any` function and a generator expression to check if any value in the first sequence is present in the second sequence. If any value is found, the function returns True. If no values are found after checking all values in the first sequence, the function returns False. 

This function is more concise and efficient than the previous one, as it avoids the need for explicit iteration and uses the `any` function to simplify the logic. 

You can use this function to check if any two sequences have at least one overlapping value. For example:

```python
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
```


This function will correctly return False for the given test case, as the two sequences do not have any overlapping values. 

You can use this function to check for overlapping values in any two sequences. For example:

```python
print(overlapping([1,2,3,4,5],[4,5,6,7]))  # Returns True
print(overlapping([1,2,3,4,5],[6,7,8,9]))  # Returns False
```


This function will correctly return True for the first test case, as the two sequences have overlapping values, and False for the second test case, as the two sequences do not have any overlapping values. 

In summary, this function can be used to check if any two sequences have at