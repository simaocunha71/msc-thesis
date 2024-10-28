Here is the solution in Go:

```go
import (
    "sort"
)

func Maximum(arr []int, k int) []int {
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    return arr[:k]
}
```
This function sorts the array in descending order and then returns the first k elements. The `sort.Slice` function is used to sort the array. The sorting function takes a comparison function as an argument, which is used to determine the order of the elements. In this case, we are sorting in descending order, so the comparison function returns `true` if the first element is greater than the second element. The `[]:k` at the end of the function returns a slice of the first k elements of the sorted array. 

For example, if `arr = [-3, -4, 5]` and `k = 3`, the function will return `[-4, -3, 5]`. If `arr = [4, -4, 4]` and `k = 2`, the function will return `[4, 4]`. If `arr = [-3, 2, 1, 2, -1, -2, 1]` and `k = 1`, the function will return `[2]`. 

The time complexity of this function is O(n log n) due to the sorting operation. The space complexity is O(1) as we are not using any extra space that scales with the input. 