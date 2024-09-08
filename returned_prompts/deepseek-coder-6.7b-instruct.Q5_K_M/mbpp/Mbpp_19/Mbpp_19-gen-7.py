def test_duplicate(arr):
    return len(arr) != len(set(arr))

print(test_duplicate([1,2,3,4,5])) # False

Explanation:
The function uses a set to remove duplicate elements from the array and then compares the lengths of the original array and the set. If the lengths are equal, that means there were no duplicate elements in the array, so the function returns False. If the lengths are not equal, that means there were duplicate elements in the array, so the function returns True.


