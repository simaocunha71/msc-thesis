def test_duplicate(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False

# Test
print(test_duplicate([1, 2, 3, 4, 5]))  # False
print(test_duplicate([1, 2, 3, 4, 5, 1]))  # True

"""
The time complexity of this function is O(n) because in the worst case, we need to check each element of the list exactly once.
"""

"""
The space complexity of this function is O(n) because, in the worst-case scenario, we need to store all the elements of the list in the set.
"""

"""
Here, we are using a set data structure to keep track of all the elements we have seen so far in the list. A set is a collection of unique elements, so if an element is already in the set, we know that it's a duplicate and we can return True. Otherwise, we add the element to the set and continue iterating through the list. If we reach the end of the list and haven't found any duplicates, we return False.
"""

"""
This implementation has a time complexity of O(n) because we traverse the list once, and each element is processed in constant time. It also has a space complexity of O(n) because we store all the unique elements in the set.
"""

"""
In this function, we use a set to keep track of all the elements we have seen so far. A set is a collection of unique elements, so if an element is already in the set, we know that it's a duplicate and we can return True. Otherwise, we add the element to the set and continue iterating through the list. If we reach the end of the list and haven't found any duplicates, we return False. This implementation has a time complexity of O(n) because we traverse the list once, and each element is processed in constant time. It also has a space complexity of O(n) because we store all the unique elements in the set.
"""

"""
This function can be used to check whether a given array of integers contains any duplicate element. It returns True if there