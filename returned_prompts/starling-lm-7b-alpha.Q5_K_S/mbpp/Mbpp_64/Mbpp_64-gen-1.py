from operator import itemgetter

def subject_marks(tup_list):
    tup_list.sort(key=itemgetter(1))
    return tup_list

# Test the function
print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))

# Expected Output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
"""

# Explanation
In the given problem, we are asked to sort a list of tuples based on the second value of each tuple. To achieve this, we can use the built-in Python function `sort()` and the `itemgetter` function from the `operator` module.

The `itemgetter` function allows us to specify the index of the item we want to use for sorting. In this case, we want to sort the tuples based on the second value, so we pass `itemgetter(1)` as the key to the `sort()` function.

The `sort()` function will rearrange the tuples in the list based on the specified key, sorting them in ascending order. Finally, the sorted list is returned.

In the provided code, the `subject_marks()` function takes a list of tuples as input and sorts them using the `sort()` function with `itemgetter(1)` as the key. The sorted list is then returned.

To test the function, we call it with a sample list of tuples and print the result. The expected output is `[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]`, which is the sorted list of tuples based on the second value of each tuple.

Overall, this solution demonstrates how to sort a list of tuples based on a specific value within each tuple using the `sort()` function and `itemgetter` from the `operator` module.

"""

```python
from operator import itemgetter

def subject_marks(tup_list):
    tup_list