def recursive_list_sum(lst):
    sum = 0
    for i in lst:
        if isinstance(i, list):
            sum += recursive_list_sum(i)
        else:
            sum += i
    return sum

def test_recursive_list_sum():
    assert recursive_list_sum([1, 2, [3,4],[5,6]])==21

test_recursive_list_sum()

"""
The function recursive_list_sum() takes in a list and sums all of its elements. It does this by iterating over the list with a for loop. For each element in the list, it checks if the element is itself a list using isinstance(). If it is, then the function calls itself recursively with the sublist as the argument. If the element is not a list, it adds the element to the sum. After going through all the elements in the original list, the function returns the sum of all the elements.

The function test_recursive_list_sum() is used to test the function recursive_list_sum(). It calls recursive_list_sum() with the list [1, 2, [3,4],[5,6]] and asserts that the result is equal to 21. If the assertion is true, the test passes; if not, an AssertionError is raised.

To use the function recursive_list_sum(), you can simply call it with a list as an argument. For example, recursive_list_sum([1, 2, [3,4],[5,6]]) will return 21, as expected.
"""

# The function test_recursive_list_sum() is used to test the function recursive_list_sum(). It calls recursive_list_sum() with the list [1, 2, [3,4],[5,6]] and asserts that the result is equal to 21. If the assertion is true, the test passes; if not, an AssertionError is raised.

# To use the function recursive_list_sum(), you can simply call it with a list as an argument. For example, recursive_list_sum([1, 2, [3,4],