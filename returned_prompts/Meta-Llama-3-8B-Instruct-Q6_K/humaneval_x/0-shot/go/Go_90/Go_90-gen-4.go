Here is the Go code that solves the problem:

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

1. We first check if the length of the input list is less than 2. If it is, we return `nil` because there are not enough elements to find the 2nd smallest.
2. We sort the list in ascending order using the `sort.Ints` function.
3. We iterate through the sorted list, starting from the second element (index 1). We check if the current element is greater than the first element. If it is, we return the current element because it is the 2nd smallest.
4. If we reach the end of the list without finding a 2nd smallest element, we return `nil`. This happens when the list has only one unique element, or all elements are the same. In this case, there is no 2nd smallest element.