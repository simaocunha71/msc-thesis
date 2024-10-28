```go
func IsSorted(lst []int) bool {
    if len(lst) <= 1 {
        return true
    }
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] >= lst[i+1] {
            return false
        }
    }
    count := 1
    for i := 1; i < len(lst); i++ {
        if lst[i] == lst[i-1] {
            count++
        } else {
            if count > 1 {
                return false
            }
            count = 1
        }
    }
    return true
}
```


The function `IsSorted` takes a slice of integers as input and returns a boolean indicating whether the list is sorted in ascending order and has no more than one duplicate of the same number.

The function first checks if the length of the list is 1 or less, in which case it returns `true` since a list with one element or no elements is considered sorted.

Then it iterates through the list, checking if each element is less than or equal to the next one. If it finds a pair of elements where the first is greater than or equal to the second, it returns `false` since the list is not sorted.

After checking the list for sorting, it iterates through the list again, counting the number of consecutive duplicates. If it finds more than one consecutive duplicate, it returns `false` since the list has more than one duplicate.

If the function has not returned `false` by the end of the second loop, it returns `true` since the list is sorted and has no more than one duplicate.