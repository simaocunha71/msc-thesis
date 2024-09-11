To check whether a specified list is sorted or not, you can use the built-in Python function sorted() function. The sorted() function returns a new sorted list. If the original list is already sorted, this function will return the same list. Here is a step-by-step guide to solve this problem:

1. Define a function called issort_list that takes a list as an argument. This function will check if the list is sorted in ascending order.
2. Inside the function, use the sorted() function to create a new list that contains the elements of the original list in sorted order. Assign this new list to a variable called sorted_list.
3. Check if the sorted_list is equal to the original list. If they are equal, it means the original list is sorted. If not, it means the original list is not sorted.
4. Return True if the sorted_list is equal to the original list. Otherwise, return False.
5. Test the function by passing a sorted list to the function and asserting that the function returns True.

Here is the Python code that implements the above steps:

```python
def issort_list(lst):
    # Create a sorted list from the original list
    sorted_list = sorted(lst)
    # Check if the sorted list is equal to the original list
    if sorted_list == lst:
        return True
    else:
        return False

# Test the function with a sorted list
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
```

When you run this code, it will print "True" to the console, indicating that the function correctly determined that the list is sorted.

"""
"""

def issort_list(lst):
    if len(lst) == 0 or len(lst) == 1:
        return True
    else:
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                return False
        return True

assert issort_list([1,2,4,6,8,10,12,14,16,17])==True

"""

"""
This implementation of