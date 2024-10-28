
def search(lst):
    from collections import Counter
    count = Counter(lst)
    max_val = max(count.keys())
    for i in range(max_val, 0, -1):
        if count[i] >= i:
            return i
    return -1

print(search([4, 1, 2, 2, 3, 1])) # 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) # 3
print(search([5, 5, 4, 4, 4])) # -1


In this code, we first count the frequency of each number in the list using the Counter function from the collections module. Then we find the maximum value in the keys of the count dictionary. We start from this maximum value and iterate down to 1, checking each time whether the count of the current value is equal to or greater than the value itself. If we find such a value, we return it. If we don't find any such value, we return -1.

The time complexity of this code is O(n) because we go through the list of numbers once to count their frequencies, and then we go through the numbers from the maximum to 1, checking their counts. The space complexity is also O(n) because we store the counts of all the numbers in the list.

This code works for lists with positive integers only. If the list can contain other types of numbers or if negative numbers can be in the list, additional error checking would be needed.
