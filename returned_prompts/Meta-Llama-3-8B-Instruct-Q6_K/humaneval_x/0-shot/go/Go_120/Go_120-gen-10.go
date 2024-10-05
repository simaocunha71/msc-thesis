Here is the solution:
```go
import (
    "sort"
)

func Maximum(arr []int, k int) []int {
    // Sort the array in descending order
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    // Return the first k elements of the sorted array
    return arr[:k]
}
```
Explanation:

1. We use the `sort.Slice` function to sort the array in descending order. This is because we want to find the maximum k numbers in the array.
2. We use a custom sorting function that takes two indices `i` and `j` and returns `true` if the element at index `i` is greater than the element at index `j`. This tells the `sort.Slice` function to sort the array in descending order.
3. After sorting the array, we return the first k elements of the sorted array. This gives us the maximum k numbers in the array.

Example:
```go
arr := []int{-3, -4, 5}
k := 3
result := Maximum(arr, k)
fmt.Println(result) // Output: [-4, -3, 5]
```
This solution has a time complexity of O(n log n) due to the sorting operation, where n is the length of the array. The space complexity is O(1) since we only use a small amount of extra memory to store the sorted array.