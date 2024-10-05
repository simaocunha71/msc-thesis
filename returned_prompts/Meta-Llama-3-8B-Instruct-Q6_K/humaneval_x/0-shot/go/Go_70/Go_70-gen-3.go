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

This function uses the sort.Slice function to sort the list. The sorting function is a closure that takes two indices i and j. It returns true if the element at index i should come before the element at index j in the sorted list.

In the sorting function, we check if the index i is even or odd. If i is even, we compare the elements at indices i and j in ascending order. If i is odd, we compare the elements at indices i and j in descending order.

This way, the list is sorted in the "strange" order, where the minimum value comes first, then the maximum value of the remaining integers, then the minimum value of the remaining integers, and so on. The function returns the sorted list. If the input list is empty, the function returns an empty list.