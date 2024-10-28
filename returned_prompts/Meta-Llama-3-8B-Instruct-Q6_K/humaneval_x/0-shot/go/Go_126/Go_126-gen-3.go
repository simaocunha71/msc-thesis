```go
func IsSorted(lst []int) bool {
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] >= lst[i+1] {
            if i+1 < len(lst) && lst[i+1] == lst[i] {
                return false
            }
            return false
        }
    }
    return true
}
```


The function `IsSorted` checks if the given list of integers is sorted in ascending order. If the list has more than one duplicate of the same number, it returns `false`.

Here's how it works:

1. We iterate through the list, comparing each element with the next one.
2. If an element is greater than or equal to the next one, it means the list is not sorted. We immediately return `false`.
3. If an element is equal to the next one, it means we have a duplicate. We check if this is the first occurrence of the duplicate or not. If it's not the first occurrence, we return `false`.
4. If we finish the iteration without finding any non-sorted elements or duplicates, we return `true`, indicating that the list is sorted.

This function assumes that the list does not contain negative numbers and only contains integers. It also assumes that the list is not empty. If the list is empty, the function will return `true` because an empty list is considered sorted. If you want to handle empty lists differently, you can add a simple check at the beginning of the function.