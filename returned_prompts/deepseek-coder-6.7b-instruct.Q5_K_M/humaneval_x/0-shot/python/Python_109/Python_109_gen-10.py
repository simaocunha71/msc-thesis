
def move_one_ball(arr):
    if not arr: return True
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            count += 1
    return count <= 1

print(move_one_ball([3, 4,_ 5, 1, 2]))
print(move_one_ball([3, 5, 4, 1, 2]))
print(move_one_ball([]))

Explanation:

The function `move_one_ball` takes in an array `arr` and returns True if it's possible to sort the array by shifting elements in the array.

It first checks if the array is empty and if so, returns True.

Then, it counts the number of times the current element is greater than the next element. This is because we can only perform a shift if the current element is greater than the next.

Finally, it returns True if the number of shifts is less than or equal to 1 and False otherwise. This is because we can perform at most one shift to sort the array.



Test Cases:

move_one_ball([3, 4, 5, 1, 2]) returns: True
move_one_ball([3, 5, 4, 1, 2]) returns: False
move_one_ball([]) returns: True

"""


def move_one_ball(arr):
    if not arr:
        return True
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            count += 1
    return count <= 1


print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False
print(move_one_ball([]))  # True

# Solution 2

def move_one_ball(arr):
    if not arr: return True
    return sum(i > j for i, j in zip(arr, arr[