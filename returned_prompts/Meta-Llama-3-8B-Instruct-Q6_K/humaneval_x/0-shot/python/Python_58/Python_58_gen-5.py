    return sorted(set(l1) & set(l2))


This function takes two lists as input and returns a sorted list of unique common elements. The `set` function is used to convert the lists to sets, which are unordered collections of unique elements. The `&` operator is used to find the intersection of the two sets, which are the common elements. The `sorted` function is used to sort the resulting list.

The time complexity of this function is O(n), where n is the length of the longer list, because set operations take linear time. The space complexity is also O(n), because we need to store the sets and the resulting list.

The doctests provided demonstrate the function's behavior with different inputs. The first test case shows that the function returns a list of unique common elements in the correct order. The second test case shows that the function returns a list of common elements even if they appear multiple times in the input lists. The third test case shows that the function returns an empty list if there are no common elements.