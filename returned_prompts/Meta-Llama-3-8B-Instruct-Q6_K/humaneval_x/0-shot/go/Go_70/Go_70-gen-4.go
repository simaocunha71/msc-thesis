Here is a solution that uses a simple loop to iterate through the list, sorting it in the "strange" order:

```go
import (
    "sort"
)

// Given list of integers, return list in strange order.
// Strange sorting, is when you start with the minimum value,
// then maximum of the remaining integers, then minimum and so on.
// 
// Examples:
// StrangeSortList([1, 2, 3, 4]) == [1, 4, 2, 3]
// StrangeSortList([5, 5, 5, 5]) == [5, 5, 5, 5]
// StrangeSortList([]) == []
func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return []int{}
    }

    sort.Ints(lst)
    var result []int

    for len(lst) > 0 {
        if len(lst) == 1 {
            result = append(result, lst[0])
            lst = []int{}
        } else {
            min := lst[0]
            max := lst[0]
            for _, num := range lst {
                if num < min {
                    min = num
                }
                if num > max {
                    max = num
                }
            }
            result = append(result, min)
            lst = append([]int{}, lst[1:]...)
            lst = append(lst, max)
        }
    }

    return result
}
```

This solution first sorts the list in ascending order using the `sort.Ints` function. Then it iterates through the list, always taking the smallest remaining number and the largest remaining number, and appending them to the result list. If there is only one number left in the list, it is appended to the result list. Finally, the result list is returned.