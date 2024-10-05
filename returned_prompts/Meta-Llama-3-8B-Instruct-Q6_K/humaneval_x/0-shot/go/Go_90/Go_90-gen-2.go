Here is the solution:

```go
import (
    "math"
    "sort"
)

func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    for i := 1; i < len(lst); i++ {
        if lst[i] > lst[0] {
            return lst[i]
        }
    }
    return nil
}
```

Explanation:

1. First, we check if the length of the input list is less than 2. If it is, we return nil because there is no 2nd smallest element.
2. We sort the list in ascending order using the sort.Ints function.
3. We then iterate through the sorted list starting from the 2nd element (index 1).
4. If we find an element that is greater than the smallest element (which is at index 0), we return that element as the 2nd smallest element.
5. If we reach the end of the list without finding a 2nd smallest element, we return nil.

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the length of the input list. The subsequent iteration through the list has a time complexity of O(n). Therefore, the overall time complexity is O(n log n). The space complexity is O(1) as we only use a fixed amount of space to store the input list and the temporary variables. 