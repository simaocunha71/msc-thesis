
def strange_sort_list(lst):
    sorted_list = []
    while lst:
        min_val = min(lst)
        sorted_list.append(min_val)
        lst.remove(min_val)
        if lst:
            max_val = max(lst)
            lst.remove(max_val)
            sorted_list.append(max_val)
    return sorted_list

strange_sort_list([1, 2, 3, 4])
# Output: [1, 4, 2, 3]

strange_sort_list([5, 5, 5, 5])
# Output: [5, 5, 5, 5]

strange_sort_list([])
# Output: []


def strange_sort_list(lst):
    sorted_list = []
    while lst:
        min_val = min(lst)
        sorted_list.append(min_val)
        lst.remove(min_val)
        if lst:
            max_val = max(lst)
            lst.remove(max_val)
            sorted_list.append(max_val)
    return sorted_list

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)

# This is a brute force solution.
# It's not the most efficient solution,
# but it is a simple solution that is easy to understand.

# The time complexity of this solution is O(nlog(n)) because
# the min function and max function have a time complexity of O(log(n)).

# The space complexity of this solution is O(n) because
# a new list is created to store the sorted values.

# This solution is not the most efficient,
# but it is a simple and easy to understand solution.

# There are more efficient solutions available,
# but they are more complex and harder to understand.

# This solution is suitable for small lists of integers,
# but for larger lists, a more efficient solution should be used.

# This solution is suitable for small lists of integers,
# but for larger lists,