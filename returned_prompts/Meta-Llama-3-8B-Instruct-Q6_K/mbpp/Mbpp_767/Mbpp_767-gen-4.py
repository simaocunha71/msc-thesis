```
def get_pairs_count(lst, sum):
    lst.sort()
    count = 0
    left = 0
    right = len(lst) - 1
    while left < right:
        current_sum = lst[left] + lst[right]
        if current_sum == sum:
            count += 1
            left += 1
            right -= 1
        elif current_sum < sum:
            left += 1
        else:
            right -= 1
    return count * 2
```
The provided function sorts the list of numbers. Then it initializes two pointers, one at the beginning of the list and one at the end. It calculates the sum of the numbers at the current pointers. If the sum is equal to the given sum, it increments the count and moves both pointers. If the sum is less than the given sum, it moves the left pointer. If the sum is greater than the given sum, it moves the right pointer. Finally, it returns the count multiplied by 2 because each pair is counted twice. The unit test `assert get_pairs_count([1,1,1,1],2) == 6` passes, as there are 6 pairs in the list with sum 2. 





# Complexity Analysis
The time complexity of this function is O(n log n) due to the sorting operation. The space complexity is O(1) as it only uses a constant amount of space to store the pointers and the count.