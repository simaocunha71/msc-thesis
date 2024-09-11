def swap_List(lst):
    # Create a copy of the list
    lst_copy = lst[:]
    # Swap the first and last elements
    lst_copy[0], lst_copy[-1] = lst_copy[-1], lst_copy[0]
    # Return the modified list
    return lst_copy

# Test the function
print(swap_List([12, 35, 9, 56, 24])) # Output: [24, 35, 9, 56, 12]

# Assertion
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]







"""
The provided Python function, `swap_List`, takes a list as input and returns a new list with the first and last elements swapped. Here's how the function works:

1. It creates a copy of the input list using the `[:]` slicing syntax. This is important because modifying the original list directly would not satisfy the requirement of returning a new list.

2. It swaps the first and last elements of the copied list using a single line of code: `lst_copy[0], lst_copy[-1] = lst_copy[-1], lst_copy[0]`. This uses tuple unpacking to assign the values of `lst_copy[-1]` to `lst_copy[0]` and vice versa.

3. It returns the modified list, `lst_copy`.

To test the function, you can call it with a sample list, such as `[12, 35, 9, 56, 24]`. The function will return a new list with the first and last elements swapped, which you can then print to verify the result.

To ensure the correctness of the function, you can use the `assert` statement to check if the returned list matches the expected output. In this case, you can assert that `swap_List([12, 35, 9, 56, 24])` is equal to `[24, 3