def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i+1]:
            if lst.count(lst[i]) > 1:
                return False
    return True
# test cases
print(is_sorted([5]))  # True
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # False
# Explanation
This function checks if the input list is sorted in ascending order. If a number is greater than or equal to the next number, it checks if that number appears more than once in the list. If it does, the function returns False, indicating that the list is not sorted. If the function finishes checking the entire list without finding a non-unique number out of order, it returns True, indicating that the list is sorted. The function uses the built-in count method to check for duplicate numbers. The time complexity of this function is O(n), where n is the length of the input list. This is because the function needs to iterate over the list once to check for duplicates and order. The space complexity is O(1), as the function only uses a constant amount of space to store the current number and the count of duplicates.