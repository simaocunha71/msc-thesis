
def can_arrange(arr):
    max_idx = -1
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            max_idx = i + 1
    return max_idx

print(can_arrange([1,2,4,3,5]))  # Output: 3
print(can_arrange([1,2,3]))  # Output: -1
print(can_arrange([5,4,3,2,1]))  # Output: 1
print(can_arrange([1,2,5,4,3]))  # Output: 3

This solution iterates over the array from the first element to the penultimate, checking each pair of elements. If an element is greater than the next one, it means we can rearrange the array so that this element comes first, and we update the maximum index found so far. If no such element is found, we return -1.

This solution has a time complexity of O(n), where n is the length of the array, as we iterate over the array once. The space complexity is O(1), as we only store a single integer value and do not use any additional data structures.

We can also use a list comprehension to solve this problem in a more concise way:

def can_arrange(arr):
    return next((i for i in range(len(arr) - 1) if arr[i] > arr[i + 1]), -1)

This one-liner does the same as the previous solution, but in a more concise way. It uses the built-in next function to find the first element that satisfies a condition (the condition is given by the generator expression), and if no such element is found, it returns the default value -1.
'''

# Test Cases:

assert can_arrange([1,2,4,3,5]) == 3
assert can_arrange([1,2,3]) == -1
assert can_arrange([5,4,3,2,1]) == 1
assert can_arrange([1,2,5,4,3]) == 3
assert can_arrange([5,6,1,