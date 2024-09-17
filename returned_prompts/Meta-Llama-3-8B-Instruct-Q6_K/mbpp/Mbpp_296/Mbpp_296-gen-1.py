The problem is asking to write a function that counts the number of inversions in an array. An inversion is an ordered pair of elements in the array where the first element is greater than the second element. For example, in the array [1,20,6,4,5], there are five inversions: (20,1), (20,6), (20,4), (6,1), and (6,4).

Here is a Python function that solves this problem:
```
def get_Inv_Count(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count
```
This function works by iterating over the array and checking each pair of elements. If the first element is greater than the second element, it increments the inversion count.

The unit test `assert get_Inv_Count([1,20,6,4,5]) == 5` ensures that the function is working correctly. This test checks that the function returns 5 for the input array [1,20,6,4,5], which is the correct number of inversions in this array.

This solution has a time complexity of O(n^2) because it uses two nested loops to iterate over the array. This may not be efficient for large arrays. A more efficient solution would be to use a divide-and-conquer approach, but this would be more complex to implement.