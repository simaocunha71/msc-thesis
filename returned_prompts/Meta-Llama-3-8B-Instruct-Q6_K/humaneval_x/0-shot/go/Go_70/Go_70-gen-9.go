Here is the solution in Go:

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

In this solution, we use the `sort.Slice` function to sort the list. The comparison function takes two indices `i` and `j` and returns a boolean indicating whether the `i-th` element should come before the `j-th` element.

We use the modulo operator `%` to determine whether the current index `i` is even or odd. If it's even, we sort the list in ascending order (i.e., `lst[i] < lst[j]`). If it's odd, we sort the list in descending order (i.e., `lst[i] > lst[j]`).

Finally, we return the sorted list. If the input list is empty, we return an empty list. Otherwise, we sort the list and return it.