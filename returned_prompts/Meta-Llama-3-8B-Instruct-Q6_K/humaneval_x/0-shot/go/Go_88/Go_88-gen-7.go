Here is the solution in Go:
```go
import (
    "sort"
)

func SortArray(array []int) []int {
    sum := array[0] + array[len(array)-1]
    if sum%2 == 0 {
        sort.Slice(array, func(i, j int) bool {
            return array[i] < array[j]
        })
    } else {
        sort.Slice(array, func(i, j int) bool {
            return array[i] > array[j]
        })
    }
    return array
}
```
Explanation:

1. Calculate the sum of the first and last elements of the array.
2. If the sum is even, sort the array in ascending order.
3. If the sum is odd, sort the array in descending order.
4. Return the sorted array.

Note: The `sort.Slice` function is used to sort the array in place. The comparison function is used to determine the order of sorting. In this case, we use a simple comparison function that returns `true` if the element at index `i` is less than the element at index `j`, and `false` otherwise. This is equivalent to sorting in ascending order. If we want to sort in descending order, we simply swap the comparison operators (`<` and `>`).