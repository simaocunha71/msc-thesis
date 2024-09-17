You can use the following Python function to locate the right insertion point for a specified value in sorted order:

```Python
def right_insertion(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```
This function uses a binary search approach to find the right insertion point for the target value in the sorted array. It returns the index where the target value should be inserted to maintain the sorted order.

For example, if you call `right_insertion([1,2,4,5],6)`, it will return `4`, which is the index where `6` should be inserted to maintain the sorted order. 

This solution works in O(log n) time, where n is the number of elements in the array, making it efficient for large arrays. The unit test `assert right_insertion([1,2,4,5],6)==4` ensures that the function works correctly. 

Please note that this function assumes that the input array is already sorted. If the array is not sorted, you need to sort it first before calling this function.  If you want to insert the target value into the array and maintain the sorted order, you can use the following code:

```Python
def right_insertion(arr, target):
    arr.append(target)
    arr.sort()
    return arr
``` 

However, this solution works in O(n log n) time, where n is the number of elements in the array, because the sort operation takes O(n log n) time. The binary search approach in the first solution is more efficient when the array is large.  If you need to insert many values into the array, you may want to consider using a balanced binary search tree data structure like AVL tree or Red-black tree, which can insert and search values in O(log n) time.  If you need to insert and search values frequently, you may want to consider using a hash table data structure like dictionary in Python, which can insert and search values in O(1) time on average.  However, the hash table data structure requires more memory to store the hash table.  The choice of data structure depends on the specific requirements of your application.  If the array is large and you need to insert and search values frequently,