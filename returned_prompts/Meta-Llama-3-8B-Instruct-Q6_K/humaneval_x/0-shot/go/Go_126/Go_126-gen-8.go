Here is a Go function that fulfills the requirements:

```go
func IsSorted(lst []int) bool {
    for i := 1; i < len(lst); i++ {
        if lst[i] <= lst[i-1] {
            if i > 1 && lst[i] == lst[i-1] {
                return false
            }
            return false
        }
    }
    return true
}
```

In this function, we iterate over the list starting from the second element (index 1). For each element, we check if it's less than or equal to the previous element. If it is, we return false because the list is not sorted. If it's not, we continue to the next iteration.

If we reach the end of the list without returning false, it means the list is sorted, so we return true.

The condition `i > 1 && lst[i] == lst[i-1]` is used to check if there are duplicate elements in the list. If there are, we return false. This condition is only checked when `i` is greater than 1, because the first element can't be a duplicate.