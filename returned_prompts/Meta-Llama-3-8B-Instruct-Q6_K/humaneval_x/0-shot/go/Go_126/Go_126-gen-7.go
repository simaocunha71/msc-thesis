```go
func IsSorted(lst []int) bool {
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] >= lst[i+1] {
            if i > 0 && lst[i] == lst[i-1] {
                return false
            }
            return false
        }
    }
    return true
}
```


This solution iterates through the list of numbers, checking if each element is less than the next one. If it finds a pair of elements where the first is greater than or equal to the second, it immediately returns `false`, as the list is not sorted.

However, if the list is sorted, it also checks if there are any duplicates. If it finds a duplicate (i.e., the current element is the same as the previous one), it returns `false`, as the list is not sorted.

If the function reaches the end of the list without finding any elements that are not in sorted order or any duplicates, it returns `true`, indicating that the list is sorted.