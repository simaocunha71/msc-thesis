```
func IsSorted(lst []int) bool {
    if len(lst) <= 1 {
        return true
    }
    for i := 1; i < len(lst); i++ {
        if lst[i] <= lst[i-1] {
            return false
        }
    }
    return true
}
```



Explanation:
The function `IsSorted` takes a slice of integers as input and returns a boolean indicating whether the list is sorted in ascending order.

The base case is when the length of the list is 0 or 1, in which case the function returns `true` since a list with 0 or 1 elements is considered sorted.

The main logic is implemented in the for loop, which iterates over the list starting from the second element (index 1). For each element, it checks if the current element is less than or equal to the previous element. If this condition is met, it means the list is not sorted, so the function returns `false`.

If the loop completes without finding any elements that are less than or equal to the previous element, it means the list is sorted, so the function returns `true`.

The function also checks for duplicate elements by comparing each element with the previous one. If a duplicate element is found, the function returns `false`. However, this check is not necessary in this specific problem since the problem statement assumes no negative numbers and only integers. If the list has more than one duplicate of the same number, the function will still return `false`.