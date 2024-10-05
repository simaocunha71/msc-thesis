You can achieve this by creating two slices, one for the minimum values and one for the maximum values. After that, you can combine the two slices in alternating order to get the desired output.

Here is the implementation:

```go
import (
    "sort"
)

func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return lst
    }

    sort.Ints(lst)

    minList := make([]int, 0)
    maxList := make([]int, 0)

    min, max := 0, len(lst)-1
    for min <= max {
        minList = append(minList, lst[min])
        if min != max {
            maxList = append(maxList, lst[max])
        }
        min++
        max--
    }

    result := make([]int, 0)
    for i := 0; i < len(minList); i++ {
        result = append(result, minList[i])
        if i < len(maxList) {
            result = append(result, maxList[i])
        }
    }

    return result
}
```

This implementation first sorts the input list in ascending order. Then it creates two slices, one for the minimum values and one for the maximum values. The minimum value is added to the `minList` and the maximum value is added to the `maxList` in alternating order. Finally, the two slices are combined to get the desired output.

Please let me know if you need any further assistance!