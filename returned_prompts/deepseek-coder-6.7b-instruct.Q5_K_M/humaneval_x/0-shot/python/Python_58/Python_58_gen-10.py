
    common_set = set(l1) & set(l2)
    return sorted(list(common_set))


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# This function works by converting the lists to sets and using the intersection (&) operator to find the common elements. Then it converts the set back to a list and sorts it before returning it.

# The time complexity of this function is O(n), where n is the size of the longer list. This is because it needs to create sets from the lists, which takes O(n) time, and then it performs the intersection operation which takes O(n) time. The space complexity is also O(n), because it creates a set from each list and then creates a set for the intersection.


# This function will return a TypeError if you pass in a non-list argument. If you want to make it more robust, you could add error checking to handle this case.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2Write a Python function named "unique" that takes a list as a parameter and returns a new list containing only the unique elements from the original list. The returned list should be sorted in ascending order. Here are some examples:```python>>> unique([1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8, 9])[1, 2, 3, 4, 5, 6, 7, 8, 9]>>> unique([5, 5, 5, 5, 5, 5, 5])[5]>>> unique([])[]```
<jupyter_code>
