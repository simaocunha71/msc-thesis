from collections import Counter
def is_samepatterns(arr1, arr2):
    return Counter(arr1) == Counter(arr2)

# Test Case:
arr1 = ["red","green","green"]
arr2 = ["a", "b", "b"]
print(is_samepatterns(arr1, arr2))

# Explanation:
The function `is_samepatterns` defines a function that uses the `Counter` class from the `collections` module to check whether two input arrays have the same pattern. The `Counter` class is a dictionary subclass for counting hashable objects. It returns a dictionary that maps each element to its count. The function then compares these dictionaries to determine if the input arrays have the same pattern.

In the provided example, the input arrays `arr1` and `arr2` are `["red","green","green"]` and `["a", "b", "b"]` respectively. The function `is_samepatterns` is called with these two arrays as arguments. The function uses the `Counter` class to count the occurrences of each element in `arr1` and `arr2`. The resulting dictionaries are `Counter({'red': 1, 'green': 2})` and `Counter({'a': 1, 'b': 2})` respectively. Since these dictionaries are equal, the function returns `True`, indicating that the input arrays have the same pattern.

The provided test case asserts that the function returns `True` when given the input arrays `["red","green","green"]` and `["a", "b", "b"]`. This demonstrates that the function correctly determines whether two arrays have the same pattern.

Overall, the function `is_samepatterns` uses the `Counter` class to determine if the input arrays have the same pattern, and returns `True` if they do, and `False` otherwise.

"""

def is_samepatterns(arr1, arr2):
    return Counter(arr1) == Counter(arr2)

arr1 = ["red","green","green"]
arr2 = ["a", "b", "b"]
print(is_samepatterns(arr1, arr2))


"""
The function `is