Here is the solution:

```go
import (
    "sort"
)

// Given list of integers, return list in strange order.
// Strange sorting, is when you start with the minimum value,
// then maximum of the remaining integers, then minimum and so on.
// 
// Examples:
// StrangeSortList([1, 2, 3, 4]) == [1, 4, 2, 3]
// StrangeSortList([5, 5, 5, 5]) == [5, 5, 5, 5]
// StrangeSortList([]) == []
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

Explanation:
The problem can be solved by using the built-in sort function in Go. The sort function can be used to sort the slice of integers in-place. The function takes a slice of integers and a function that defines the sort order as arguments.

The function that defines the sort order is a closure that takes two indices i and j as arguments. The function returns true if the element at index i should come before the element at index j in the sorted slice, and false otherwise.

In this case, the function will return true if the element at index i is less than the element at index j, and false otherwise. This means that the smallest element will come first, then the largest element, and so on.

To achieve the "strange" sorting order, we need to alternate between sorting the elements in ascending and descending order. This can be done by checking if the index i is even or odd. If i is even, we sort the elements in ascending order, and if i is odd, we sort the elements in descending order.

The sort function will then use this function to determine the order of the elements in the slice, resulting in the desired "strange" sorting order.

Finally, the sorted slice is returned. If the input slice is empty, the function will return an empty slice. If the input slice contains only one element, the function will return the same slice (since there is nothing to sort). Otherwise, the function will return the sorted slice.