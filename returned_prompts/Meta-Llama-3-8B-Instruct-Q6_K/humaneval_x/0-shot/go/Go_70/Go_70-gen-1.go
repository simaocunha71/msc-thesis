Here is the solution in Go:
```go
import (
    "sort"
)

func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return []int{}
    }

    sortSlice := make([]int, len(lst))
    copy(sortSlice, lst)

    sort.Slice(sortSlice, func(i, j int) bool {
        if i%2 == 0 {
            return sortSlice[i] <= sortSlice[j]
        } else {
            return sortSlice[i] >= sortSlice[j]
        }
    })

    return sortSlice
}
```
Explanation:
We create a copy of the input list and sort it using the `sort.Slice` function. We use a custom comparison function that checks if the index `i` is even or odd. If `i` is even, we sort the slice in ascending order (minimum value first), otherwise we sort it in descending order (maximum value first). The `copy` function is used to copy the input list to the `sortSlice` variable. Finally, we return the sorted slice.

Note that this solution has a time complexity of O(n log n) due to the sorting operation. If the input list is very large, this solution may be inefficient. In that case, a more efficient solution would be to use a different sorting algorithm, such as insertion sort or merge sort, which have a time complexity of O(n). However, for small to medium-sized lists, this solution should be sufficient.