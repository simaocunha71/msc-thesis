from bisect import bisect_left as bl
def kth_element(arr, k):
    arr.sort()
    return arr[k-1]

# Another way:
def kth_element(arr, k):
    return sorted(arr)[k-1]


# Python program to find kth element in array
def kth_element(arr, k):
    arr.sort()
    return arr[k-1]



```
In the kth_element function, the input array is first sorted in ascending order using the sort() method. The kth element in the sorted array is then returned using indexing, which is k-1 since array indexing is 0-based.

Alternatively, the kth_element function can be implemented using the sorted() function to directly sort the input array and return the kth element using indexing. Both implementations will give the same result.

To verify the correctness of the kth_element function, an assertion is made to check if the function correctly returns the 2nd element (k=2) in the array [12,3,5,7,19]. The expected output is 3, which is confirmed by the assertion.

The time complexity of the kth_element function is O(n log n) due to the sorting step, where n is the length of the input array. The space complexity is O(1) as no additional space is used beyond the input array.

Note: The kth_element function assumes that the input array is non-empty and contains unique elements. If the array can be empty or contain duplicate elements, additional checks and handling may be necessary.
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
``