```
func IsSorted(lst []int) bool {
    if len(lst) <= 1 {
        return true
    }
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] > lst[i+1] {
            return false
        }
        if i < len(lst)-2 && lst[i] == lst[i+1] {
            return false
        }
    }
    return true
}
```



Here is a Go solution that checks if the list is sorted and has no duplicates.

The function `IsSorted` takes a slice of integers as an argument. It first checks if the list has one or zero elements. If it does, it returns `true` as there is nothing to check.

Then it iterates over the list. If it finds a pair of consecutive elements where the first is greater than the second, it returns `false` as the list is not sorted.

It also checks for duplicates. If it finds a duplicate, it returns `false` as the list has duplicates.

If the function finishes checking the list without finding any issues, it returns `true` as the list is sorted and has no duplicates.

Here is the code:

```go
func IsSorted(lst []int) bool {
    if len(lst) <= 1 {
        return true
    }
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] > lst[i+1] {
            return false
        }
        if i < len(lst)-2 && lst[i] == lst[i+1] {
            return false
        }
    }
    return true
}
```



For example, the call `IsSorted([]int{5})` returns `true`, as the list is sorted and has no duplicates. The call `IsSorted([]int{1, 3, 2, 4, 5})` returns `false`, as the list is not sorted. The call `IsSorted([]int{1, 2, 2, 3, 3, 4})` returns `false`, as the list has duplicates. The call `IsSorted([]int{1, 2, 3, 4, 5})` returns `true`, as the list is sorted and has no duplicates.