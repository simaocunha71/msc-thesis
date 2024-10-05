```go
func IsSorted(lst []int) bool {
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] > lst[i+1] {
            return false
        }
        if i < len(lst)-2 {
            for j := i + 1; j < len(lst); j++ {
                if lst[i] == lst[j] {
                    return false
                }
            }
        }
    }
    return true
}
```



Explanation:

The function `IsSorted` takes a slice of integers as input and returns a boolean value indicating whether the list is sorted in ascending order. If the list has more than one duplicate of the same number, it returns `false`.

The function iterates through the list, checking each element against the next one. If it finds an element that is greater than the next one, it returns `false` because the list is not sorted.

For each element, it also checks if there are any duplicates in the rest of the list. If it finds a duplicate, it returns `false` because the list is not sorted.

If the function finishes iterating through the list without finding any unsorted elements or duplicates, it returns `true` because the list is sorted.

Note: The function assumes that the input list contains only positive integers. If the list can contain negative numbers or zero, the function needs to be modified accordingly.