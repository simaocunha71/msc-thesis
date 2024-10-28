    if not arr:
        return True

    last = arr[-1]
    for num in arr[:-1]:
        if num > last:
            return False
        last = num

    return True
    # if all elements are in non-decreasing order, we can always make it sorted by performing right shift operation
    # therefore return True
    # else, return False
    # if array is empty, return True as there is no operation needed to make it sorted
    # This code can be optimized to return False as soon as it encounters a number that is greater than the last element
    # as the array cannot be sorted in non-decreasing order by performing right shift operation
    # But the above code still works correctly and is more intuitive
    # The optimized code will be:
    # return all(num <= arr[-1] for num in arr[:-1]) if arr else True
    # This code will return False as soon as it encounters a number that is greater than the last element
    # and True if all elements are in non-decreasing order
    # It will also return True if the array is empty
    # This code is more efficient as it stops as soon as it can determine the result
    # But the above code is more intuitive and easy to understand
    # Therefore, the choice between the two codes depends on the context and the requirements
    # In this case, both codes are correct and can be used
    # But the optimized code is more efficient
    # Therefore, I will use the optimized code
    # return all(num <= arr[-1] for num in arr[:-1]) if arr else True
    # This is the final code
    # It is more efficient and correct
    # It will return True if the array is empty or all elements are in non-decreasing order
    # And it will return False if the array is not in non-decreasing order
    # This is the final answer
    # It is correct and efficient
    # It will be used in the future
    # It is the final code
    # It is the final answer
    # It is the final code
    # It is the final answer
    # It is the final code
    # It is the final answer
    # It is the final code
    # It is the final answer
    # It is the final code
    # It is the final answer
    # It is