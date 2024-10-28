
def search(lst):
    from collections import Counter
    count_dict = Counter(lst)
    for i in sorted(count_dict.keys(), reverse=True):
        if i <= count_dict[i]:
            return i
    return -1

print(search([4, 1, 2, 2, 3, 1]))  # 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # 3
print(search([5, 5, 4, 4, 4]))  # -1


Explanation:

The solution uses the built-in Counter class from the collections module to count the frequency of each integer in the list. The Counter class returns a dictionary where keys are the unique elements in the list and values are their counts.

The function then iterates over the keys in the dictionary in descending order (from the highest key to the lowest), because we want to find the greatest integer that has a frequency greater than or equal to the value of the integer itself.

If it finds a key that is less than or equal to its count (i.e., frequency), it returns this key as the answer. If it doesn't find such a key after checking all the elements, it returns -1.

This solution has a time complexity of O(n log n) due to the sorting of keys, where n is the length of the list. The space complexity is O(n) due to the storage of the dictionary.

Note: This solution assumes that the input list contains only positive integers. If the input can contain zero or negative integers, the function should be modified accordingly.


def search(lst):
    from collections import Counter
    count_dict = Counter(lst)
    for i in sorted(count_dict.keys(), reverse=True):
        if i > 0 and i <= count_dict[i]:
            return i
    return -1

print(search([4, 1, 2, 2, 3, 1]))  # 2
print(search([1, 2,0, 2, 3, 3, 3, 4, 4,