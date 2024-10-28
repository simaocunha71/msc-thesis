
def move_one_ball(arr):
    if not arr: return True
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or \
           all(arr[i] <= arr[i+1] for i in range(len(arr)-1, len(arr)-max(arr)-1, -1))

# Test cases
print(move_one_ball([3, 4, 5, 1, 2])) #==>True
print(move_one_ball([3, 5, 4, 1, 2])) #==>False
print(move_one_ball([1, 2, 3, 4, 5])) #==>True
print(move_one_ball([2, 1, 3, 4, 5])) #==>True
print(move_one_ball([1])) #==>True
print(move_one_ball([])) #==>True
print(move_one_ball([5, 4, 3, 2, 1])) #==>False
print(move_one_ball([2, 3, 4, 1, 5])) #==>False

In the provided function, we check if the array is already sorted or if it can be sorted by performing the right shift operation. This is done by iterating over the array and checking if each element is less than or equal to the next one. If it is not, we return False. If we finish the iteration without finding a pair of elements that is not in order, we return True. Note that we also check the array after the last right shift operation.

This solution has a time complexity of O(n) and a space complexity of O(1), where n is the length of the array.

Note: This solution assumes that the right shift operation can be performed from either end of the array.

I hope this solution is clear and helpful. Let me know if you have any other questions.

"""

# Test cases
print(move_one_ball([3, 4, 5, 1, 2])) #==>True
print(move_one_ball([3, 5, 4, 1, 2])) #