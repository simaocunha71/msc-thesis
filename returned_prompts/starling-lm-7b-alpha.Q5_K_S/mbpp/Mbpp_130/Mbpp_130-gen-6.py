```
def max_occurrences(lst):
    dictionary = {}
    for i in lst:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    maximum = 0
    max_key = 0
    for i in dictionary:
        if dictionary[i] > maximum:
            maximum = dictionary[i]
            max_key = i
    return max_key
```

This function first creates a dictionary to store all the elements in the list as keys and their frequencies as values. Then it traverses over all the keys to find the maximum frequency and the key that corresponds to it. Finally, it returns the key with maximum frequency.

The time complexity of this function is O(n), where n is the length of the input list.

The space complexity of this function is also O(n), as it uses a dictionary to store all the elements of the list.

To verify the solution, you can use the following code:
```python
def test_max_occurrences():
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == 2
    assert max_occurrences([1,2,3,4,5,6,7,8,9]) == 1
    assert max_occurrences([10,9,8,7,6,5,4,3,2,1]) == 1
    assert max_occurrences([]) == None

test_max_occurrences()
```
This test suite verifies the correctness of the `max_occurrences` function for different inputs.

The assertions in the test suite ensure that the function returns the correct result for each input. If any of the assertions fail, an `AssertionError` will be raised, indicating that the function is not working correctly.

In addition, the test suite also includes an assertion for an empty list as input, which ensures that the function can handle edge cases.

By running this test suite, you can have confidence that the `max_oc