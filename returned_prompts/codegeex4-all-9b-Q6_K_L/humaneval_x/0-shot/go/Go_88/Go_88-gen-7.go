```go
func SortArray(array []int) []int {
    sum := array[0] + array[len(array)-1]
    result := make([]int, len(array))
    copy(result, array)
    if sum%2 == 0 {
        sort.Slice(result, func(i, j int) bool {
            return result[i] > result[j]
        })
    } else {
        sort.Slice(result, func(i, j int) bool {
            return result[i] < result[j]
        })
    }
    return result
}
```

### Analysis:
The problem requires sorting an array based on the sum of its first and last elements. If the sum is even, the array should be sorted in descending order; if the sum is odd, the array should be sorted in ascending order. The solution involves calculating the sum of the first and last elements, copying the original array to a new slice, and then sorting the new slice based on the calculated sum.

### Explanation of the Code:
1. **Sum Calculation**: The sum of the first and last elements of the array is calculated using `array[0] + array[len(array)-1]`.
2. **Copy Array**: A new slice `result` is created using `copy(result, array)` to avoid modifying the original array.
3. **Sorting Condition**: The `sort.Slice` function is used to sort the `result` slice.
   - If the sum is even (`sum%2 == 0`), the array is sorted in descending order (`result[i] > result[j]`).
   - If the sum is odd (`sum%2 != 0`), the array is sorted in ascending order (`result[i] < result[j]`).
4. **Return Result**: The sorted `result` slice is returned.

This solution ensures that the original array remains unchanged and meets the problem's requirements for sorting based on the sum of the first and last elements.