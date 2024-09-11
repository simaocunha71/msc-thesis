"""
To split a given list at the nth element and add the first part to the end, you can follow the steps below:

1. Create a new list to store the elements after the nth element.
2. Use list slicing to get the elements after the nth element and add them to the new list.
3. Add the first part of the original list to the end of the new list.
4. Return the new list.

Here's a Python function that implements this approach:
"""

def split_Arr(arr,n):
    # Create a new list to store the elements after the nth element
    new_arr = []

    # Use list slicing to get the elements after the nth element and add them to the new list
    new_arr = arr[n:]

    # Add the first part of the original list to the end of the new list
    new_arr = arr[:n] + new_arr

    # Return the new list
    return new_arr

# Test the function
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]

```
  
```
def split_Arr(arr,n):
    # Create a new list to store the elements after the nth element
    new_arr = []

    # Use list slicing to get the elements after the nth element and add them to the new list
    new_arr = arr[n:]

    # Add the first part of the original list to the end of the new list
    new_arr = arr[:n] + new_arr

    # Return the new list
    return new_arr

# Test the function
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
```
```

This function takes in two parameters: `arr`, which is the original list, and `n`, which is the index of the element at which to split the list. It creates a new list called `new_arr` and uses list slicing to get the elements after the