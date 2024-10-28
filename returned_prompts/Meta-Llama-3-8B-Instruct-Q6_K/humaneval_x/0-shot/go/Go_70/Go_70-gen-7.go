Here is the solution:

```go
import (
    "sort"
)

func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return []int{}
    }
    sort.Slice(lst, func(i, j int) bool {
        if i%2 == 0 {
            return lst[i] < lst[j]
        } else {
            return lst[i] > lst[j]
        }
    })
    return lst
}
```

Explanation:
The function takes a slice of integers as input and returns a new slice with the elements in the "strange" order.

If the input slice is empty, it returns an empty slice.

Otherwise, it uses the `sort.Slice` function to sort the slice. The sorting function takes two indices `i` and `j` and returns `true` if the element at index `i` should come before the element at index `j` in the sorted slice.

The sorting function works as follows: if the index `i` is even, it compares the elements at indices `i` and `j` in ascending order (i.e., `lst[i] < lst[j]`). If the index `i` is odd, it compares the elements at indices `i` and `j` in descending order (i.e., `lst[i] > lst[j]`). This ensures that the smallest element comes first, followed by the largest element, then the second smallest, then the second largest, and so on.

Finally, the function returns the sorted slice.