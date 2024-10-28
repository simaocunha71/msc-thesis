
    from collections import Counter
    def search(lst):
        count_dict = Counter(lst)
        max_val = max(count_dict.keys())
        for i in range(max_val, 0, -1):
            if i in count_dict and count_dict[i] >= i:
                return i
        return -1

    print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
    print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
    print(search([5, 5, 4, 4, 4]))  # Output: -1

This solution works by first counting the frequency of each integer in the list using the Counter class from the collections module. Then, it iterates from the maximum key in the count_dict (which is the maximum value in lst), down to 1, and checks if there is a key in count_dict with the same value and a frequency that is greater than or equal to the key value. If it finds such a key, it returns the key. If it doesn't find any such key, it returns -1.

The time complexity of this solution is O(n), where n is the length of lst, because it uses a single pass to count the frequency of the integers and another pass to find the greatest integer that meets the condition. The space complexity is O(n) because of the space used by count_dict.

This solution assumes that the input list contains only positive integers. If the list can contain zero or negative numbers, the solution needs to be modified accordingly.
