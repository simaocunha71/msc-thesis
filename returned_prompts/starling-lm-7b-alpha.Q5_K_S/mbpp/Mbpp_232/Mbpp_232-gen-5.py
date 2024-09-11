```
def larg_nnum(li,n):
    sorted_li = sorted(li,reverse=True)
    return sorted_li[:n]
```

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

Explanation:
The function `larg_nnum` takes in a list `li` and an integer `n`. It first sorts the list `li` in descending order using the `sorted` function with the `reverse=True` parameter. Then, it returns a sublist of the sorted list containing the `n` largest items using list slicing.

In the given assertion, the function `larg_nnum` is called with the list `[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]` and the integer `2`. The expected output is `[100,90]`. This is because the list is sorted in descending order and the sublist containing the two largest items is extracted using list slicing.

The time complexity of the function is O(nlogn) because sorting the list takes O(nlogn) time. The space complexity is O(1) because no additional space is used apart from the output list.

Overall, the function `larg_nnum` efficiently solves the problem of finding the `n` largest items from a given list.

Note: The `sorted` function in Python returns a new list with the sorted elements, leaving the original list unchanged.

The provided code is a solution to the problem.

Additionally, here are some test cases for the `larg_nnum` function:
```python
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80