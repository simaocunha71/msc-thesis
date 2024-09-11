def recursive_list_sum(lst):
    res = 0
    for item in lst:
        if isinstance(item, list):
            res += recursive_list_sum(item)
        else:
            res += item
    return res

def test_recursive_list_sum():
    assert recursive_list_sum([1, 2, [3,4],[5,6]])==21

test_recursive_list_sum()

"""
The above function uses recursion to flatten the list and sum all the elements. We iterate through the list and if the current item is a list, we call the recursive_list_sum function on that item. This process continues until we reach a non-list item, at which point we add the item to the result.

The assert statement at the end is used to verify that the function works correctly. It checks if the sum of the flattened list [1, 2, [3,4],[5,6]] equals 21.
"""

"""
In the provided code, the recursive_list_sum function takes a list as an argument and returns the sum of all its elements. It uses a for loop to iterate through each item in the list. If the current item is a list, the function calls itself recursively with the item as an argument. This process continues until all nested lists are flattened into a single list. Once the function reaches a non-list item, it adds the item to the result. The function then returns the sum of all the elements.

The test_recursive_list_sum function is used to test the correctness of the recursive_list_sum function. It calls the recursive_list_sum function with the list [1, 2, [3,4],[5,6]] and checks if the returned sum is equal to 21. If the assertion fails, an AssertionError will be raised. Otherwise, the test passes.
"""

"""
The time complexity of the recursive_list_sum function is O(n), where n is the total number of elements in the list. This is because each element in the list is visited exactly once during the traversal. The space complexity is O(d), where d is the maximum depth of the nested lists