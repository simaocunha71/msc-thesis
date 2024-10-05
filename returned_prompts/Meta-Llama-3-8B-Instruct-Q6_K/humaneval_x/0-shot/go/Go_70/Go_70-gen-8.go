Here is a possible implementation of the `StrangeSortList` function in Go:
```
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
This function uses the `sort.Slice` function from the `sort` package to sort the input list. The sorting function is implemented as a closure that takes two indices `i` and `j` and returns a boolean indicating whether the element at index `i` should come before the element at index `j` in the sorted list.

In this implementation, the sorting function alternates