Here is a simple solution in Go:

```go
import (
    "sort"
)

func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return []int{}
    }
    sort.Sort(sort.IntSlice(lst))
    result := make([]int, len(lst))
    i, j := 0, len(lst)-1
    for i <= j {
        result[i] = lst[i]
        if i < j {
            result[j] = lst[j]
            j--
        }
        i++
    }
    return result
}
```

This function first sorts the list in ascending order using the `sort.Sort` function. Then it creates a new slice and fills it with elements from the original list, alternating between the smallest and the largest elements. The result is the "strange" sorted list. If the input list is empty, the function returns an empty list. 

Note: This solution assumes that the input list contains distinct integers. If the list may contain duplicate integers, the function may need to be modified to handle this case correctly. 

For example, if the input list is `[5, 5, 5, 5]`, the function will return `[5, 5, 5, 5]`, which is the original list. If the function is supposed to return a list with alternating smallest and largest elements, it would return `[5, 5, 5, 5]`. To achieve this, the function would need to be modified to keep track of the smallest and largest elements separately, and to alternate between these two elements when filling the result list.  Here is a modified version of the function that achieves this:

```go
func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return []int{}
    }
    sort.Ints(lst)
    result := make([]int, len(lst))
    smallest := 0
    largest := len(lst) - 1
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 {
            result[i] = lst[smallest]
            smallest++
        } else {
            result[i] = lst[largest]
            largest--
        }
    }
    return result
}
```

This modified function first sorts the list in ascending order. Then it creates a new slice and fills it with elements from the original list, alternating between the smallest and the largest elements. The result