Here is the solution to the problem. This function sorts the list in the "strange" order as described in the problem statement.

```go
import (
    "sort"
)

func StrangeSortList(lst []int) []int {
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

This function uses the `sort.Slice` function from the Go standard library to sort the list. The sorting function is a closure that takes two indices `i` and `j` as arguments and returns a boolean value indicating whether the element at index `i` should come before the element at index `j` in the sorted list.

The sorting function is implemented as follows:

* If the index `i` is even, the element at index `i` should come before the element at index `j` if the value of the element at index `i` is less than the value of the element at index `j`.
* If the index `i` is odd, the element at index `i` should come before the element at index `j` if the value of the element at index `i` is greater than the value of the element at index `j`.

This sorting function implements the "strange" sorting order described in the problem statement. The `sort.Slice` function uses this sorting function to sort the list in place.

Finally, the function returns the sorted list. If the input list is empty, the function returns an empty list. Otherwise, the function returns a list that is sorted in the "strange" order.