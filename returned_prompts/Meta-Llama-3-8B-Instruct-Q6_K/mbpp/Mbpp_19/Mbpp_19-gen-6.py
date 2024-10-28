```
def duplicate(lst):
    return len(lst) != len(set(lst))
```
This function works by comparing the length of the input list with the length of a set created from the list. In Python, a set is an unordered collection of unique elements, so if the list contains any duplicates, the set will have one less element than the list. The function returns True if the lengths are different (i.e., the list contains duplicates), and False otherwise.

The unit test `assert test_duplicate(([1,2,3,4,5]))==False` ensures that the function returns False for a list with no duplicates. This test is necessary because the problem description doesn't specify what the function should return if there are no duplicates. Without this test, the function could potentially return True for a list with no duplicates. 

For example, if the function simply checked if the list had more than one element, it would return True for a list with no duplicates, which is incorrect. The test ensures that the function behaves correctly in this case. 





